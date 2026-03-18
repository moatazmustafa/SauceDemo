import allure
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.ShippingPage import ShippingPage

@allure.feature("Checkout Errors")
@pytest.mark.parametrize("first, last, zip_code, error_msg", [
    ("", "Mustafa", "12345", "First Name is required"),
    ("Moataz", "", "12345", "Last Name is required"),
    ("Moataz", "Mustafa", "", "Postal Code is required"),
])
def test_shipping_missing_info(page, first, last, zip_code, error_msg):
    """
    Test case to verify error messages for missing shipping information.
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)
    shipping_page = ShippingPage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.add_to_cart("Sauce Labs Backpack")
    home_page.go_to_cart()
    cart_page.checkout()

    shipping_page.assert_loaded()
    shipping_page.fill(first, last, zip_code)
    shipping_page.continue_to_checkout()
    shipping_page.assert_error_message(error_msg)
