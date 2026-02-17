import re
import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

        # menu / logout
        self.menu_btn = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def assert_loaded(self):
        with allure.step("Assert Home page loaded (inventory)"):
          log.info("Assert Home page loaded (inventory)")
          expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
          expect(self.title).to_have_text("Products")

    def open_product(self, product_name: str):
        with allure.step(f"Open product from list: {product_name}"):
            log.info(f"Open product from list: {product_name}")
            self.page.locator("[data-test='inventory-item-name']", has_text=product_name).click()

    def go_to_cart(self):
        with allure.step("Open Cart from icon"):
            log.info("Open Cart from icon")
            self.cart_link.click()

    def logout(self):
        with allure.step("Logout from menu"):
            log.info("Logout from menu")
            self.menu_btn.click()
            self.logout_link.click()