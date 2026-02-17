import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.cart_items = page.locator("[data-test='inventory-item']")
        self.checkout_btn = page.locator("[data-test='checkout']")

    def assert_loaded(self):
        with allure.step("Check out page is loaded"):
          log.info("Check out page is loaded")
          expect(self.page).to_have_url(re.compile(r".*/cart\.html"))
          expect(self.title).to_have_text("Your Cart")

    def assert_item_present(self, product_name: str):
        with allure.step("Assert item is present in cart"):
          log.info("Assert item is present in cart")
          expect(self.page.locator("[data-test='inventory-item-name']", has_text=product_name)).to_be_visible()

    def assert_items_count(self, expected_count: int):
        with allure.step("Assert item count is equal to expected count"):
          log.info("Assert item count is equal to expected count")
          expect(self.cart_items).to_have_count(expected_count)

    def checkout(self):
        with allure.step("Click checkout button"):
          log.info("Click checkout button")
          self.checkout_btn.click()