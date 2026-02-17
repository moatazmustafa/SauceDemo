import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")

        self.item_total = page.locator("[data-test='subtotal-label']")
        self.tax = page.locator("[data-test='tax-label']")
        self.total = page.locator("[data-test='total-label']")

        self.finish_btn = page.locator("[data-test='finish']")

    def assert_loaded(self):
        with allure.step("Checkout page is loaded"):
             log.info("Checkout page is loaded")
             expect(self.page).to_have_url(re.compile(r".*/checkout-step-two\.html"))
             expect(self.title).to_have_text("Checkout: Overview")

    def assert_totals(self, total_text: str):
        # Example total_text: "Total: $43.18"
        with allure.step("Checking totals on Checkout page"):
             log.info("Checking totals on Checkout page")
             expect(self.total).to_have_text(total_text)

    def finish(self):
        with allure.step("finish checkout"):
             log.info("finish checkout")
             self.finish_btn.click()