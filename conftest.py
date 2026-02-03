import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    # 1) Decide headless or headed
    headless = os.getenv("PW_HEADLESS", "1") != "0"

    # 2) Start Playwright
    p = sync_playwright().start()

    # 3) Open browser + page
    # Always headed (browser UI)
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 4) Open the website (setup)
    page.goto("https://www.saucedemo.com/")

    # 5) Give the page to the test
    yield page

    # 6) Cleanup (teardown)
    # page.pause()   # <-- browser will stay open + inspector shows
    context.close()
    browser.close()
    p.stop()