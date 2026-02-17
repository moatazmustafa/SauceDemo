import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class ShippingPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.locator("[data-test='continue']")

    def assert_loaded(self):
        with allure.step("Assert Shipping page loaded"):
         log.info("Assert Shipping page loaded")
         expect(self.page).to_have_url(re.compile(r".*/checkout-step-one\.html"))
         expect(self.title).to_have_text("Checkout: Your Information")

    def fill(self, first: str, last: str, zip_code: str):
        with allure.step(f"Entering Shipping Details:{first} {last}"):
              log.info(f"Entering Shipping Details:{first} {last}")
              self.first_name.fill(first)
              self.last_name.fill(last)
              self.zip_code.fill(zip_code)

    def continue_to_checkout(self):
        with allure.step("Continue to Checkout"):
                log.info("Continue to Checkout")
                self.continue_btn.click()