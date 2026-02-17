import os
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from utils.logger import setup_logging
setup_logging()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Store test result on the item (item.rep_call) so fixtures can know if the test failed.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep


@pytest.fixture
def page(request):
    """
    Provide a fresh Playwright Page per test, with tracing enabled.
    On failure: save + attach trace + screenshot to Allure.
    """
    os.makedirs("artifacts/traces", exist_ok=True)
    os.makedirs("artifacts/screenshots", exist_ok=True)

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # open site
    page.goto("https://www.saucedemo.com/")

    # start tracing for every test
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    # --------- Attachments on failure ---------
    trace_path = None
    if failed:
        # 1) Screenshot file + attach to Allure
        screenshot_path = f"artifacts/screenshots/{request.node.name}_{int(time.time())}.png"
        try:
            page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(
                screenshot_path,
                name="screenshot",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            print(f"[Allure] Screenshot failed: {e}")

        # 2) Trace zip file + attach to Allure
        trace_path = f"artifacts/traces/{request.node.name}_{int(time.time())}.zip"
        try:
            context.tracing.stop(path=trace_path)
            allure.attach.file(
                trace_path,
                name="playwright-trace",
                attachment_type=AttachmentType.ZIP
            )
            print(f"\n[Saved trace] {trace_path}")
        except Exception as e:
            print(f"[Allure] Trace failed: {e}")
    else:
        # If passed, just stop tracing without saving a file
        try:
            context.tracing.stop()
        except Exception:
            pass

    # --------- Cleanup ---------
    try:
        context.close()
    except Exception:
        pass

    try:
        browser.close()
    except Exception:
        pass

    try:
        p.stop()
    except Exception:
        pass