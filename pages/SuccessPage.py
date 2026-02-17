import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class SuccessPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.header = page.locator("[data-test='complete-header']")

    def assert_loaded(self):
        with allure.step("Assert login page is loaded"):
            log.info("Assert login page is loaded")
            expect(self.page).to_have_url(re.compile(r".*/checkout-complete\.html"))
            expect(self.title).to_have_text("Checkout: Complete!")

    def assert_success_message(self):
        with allure.step("Assert success message is visible"):
                log.info("Assert success message is visible")
                expect(self.header).to_have_text("Thank you for your order!")