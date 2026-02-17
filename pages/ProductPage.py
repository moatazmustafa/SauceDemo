import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.locator("[data-test='inventory-item-name']")
        self.add_to_cart_btn = page.locator("[data-test^='add-to-cart']")
        self.back_to_products = page.locator("[data-test='back-to-products']")

    def assert_loaded(self, expected_name: str):
        with allure.step(f"Assert Product page loaded: {expected_name}"):
            with allure.step(f"Assert Product page loaded: {expected_name}"):
              log.info(f"Assert Product page loaded: {expected_name}")
              expect(self.page).to_have_url(re.compile(r".*/inventory-item\.html\?id=\d+"))
              expect(self.name).to_have_text(expected_name)

    def add_to_cart(self):
        with allure.step("Add item to cart"):
                log.info("Add item to cart")
                self.add_to_cart_btn.click()

    def back_home(self):
        with allure.step("Back to Home (Products list)"):
                log.info("Back to Home (Products list)")
                self.back_to_products.click()