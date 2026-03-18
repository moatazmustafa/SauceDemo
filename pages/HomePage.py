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
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")

        # menu / logout
        self.menu_btn = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.reset_link = page.locator("#reset_sidebar_link")

    @allure.step("Assert Home page loaded")
    def assert_loaded(self):
        with allure.step("Assert Home page loaded (inventory)"):
          log.info("Assert Home page loaded (inventory)")
          expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
          expect(self.title).to_have_text("Products")

    @allure.step("Open product: {product_name}")
    def open_product(self, product_name: str):
        with allure.step(f"Open product from list: {product_name}"):
            log.info(f"Open product from list: {product_name}")
            self.page.locator("[data-test='inventory-item-name']", has_text=product_name).click()

    @allure.step("Go to cart")
    def go_to_cart(self):
        with allure.step("Open Cart from icon"):
            log.info("Open Cart from icon")
            self.cart_link.click()

    @allure.step("Logout from app")
    def logout(self):
        with allure.step("Logout from menu"):
            log.info("Logout from menu")
            self.menu_btn.click()
            self.logout_link.click()

    @allure.step("Reset App State")
    def reset_app_state(self):
        with allure.step("Reset App State from menu"):
            log.info("Reset App State from menu")
            self.menu_btn.click()
            self.reset_link.click()
            # Close menu by clicking again or just wait for it to be done
            # Usually it's instant, but we might need to close the menu to continue interacting
            self.page.locator("#react-burger-cross-btn").click()

    @allure.step("Add product to cart: {product_name}")
    def add_to_cart(self, product_name: str):
        with allure.step(f"Add product to cart: {product_name}"):
            log.info(f"Add product to cart: {product_name}")
            item = self.page.locator("[data-test='inventory-item']", has_text=product_name)
            item.locator("button[data-test^='add-to-cart']").click()

    @allure.step("Remove product from cart: {product_name}")
    def remove_from_cart(self, product_name: str):
        with allure.step(f"Remove product from cart: {product_name}"):
            log.info(f"Remove product from cart: {product_name}")
            item = self.page.locator("[data-test='inventory-item']", has_text=product_name)
            item.locator("button[data-test^='remove']").click()

    @allure.step("Assert cart badge count: {count}")
    def assert_cart_badge(self, count: int):
        with allure.step(f"Assert cart badge count is: {count}"):
            log.info(f"Assert cart badge count is: {count}")
            expect(self.cart_badge).to_have_text(str(count))

    @allure.step("Assert cart badge is hidden")
    def assert_cart_badge_hidden(self):
        with allure.step("Assert cart badge is not visible"):
            log.info("Assert cart badge is not visible")
            expect(self.cart_badge).to_be_hidden()

    @allure.step("Sort products by: {sort_option}")
    def sort_by(self, sort_option: str):
        with allure.step(f"Sort products by: {sort_option}"):
            log.info(f"Sort products by: {sort_option}")
            # Options: az, za, lohi, hilo
            self.sort_dropdown.select_option(sort_option)

    @allure.step("Get all product names")
    def get_all_product_names(self):
        with allure.step("Get all product names from list"):
            log.info("Get all product names from list")
            return self.item_names.all_text_contents()

    @allure.step("Get all product prices")
    def get_all_product_prices(self):
        with allure.step("Get all product prices from list"):
            log.info("Get all product prices from list")
            prices = self.item_prices.all_text_contents()
            # Convert "$29.99" to float 29.99
            return [float(p.replace("$", "")) for p in prices]