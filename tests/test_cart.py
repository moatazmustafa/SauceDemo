import allure
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage

@allure.feature("Cart Management")
@allure.story("Add and Remove from Home Page")
def test_add_remove_from_home(page):
    """
    Test case to verify adding and removing items from cart on home page.
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.assert_loaded()

    product = "Sauce Labs Backpack"
    
    # Add to cart
    home_page.add_to_cart(product)
    home_page.assert_cart_badge(1)

    # Remove from cart
    home_page.remove_from_cart(product)
    home_page.assert_cart_badge_hidden()

@allure.feature("Cart Management")
@allure.story("Remove from Cart Page")
def test_remove_from_cart_page(page):
    """
    Test case to verify removing an item from the cart page.
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.assert_loaded()

    product = "Sauce Labs Bike Light"
    home_page.add_to_cart(product)
    home_page.go_to_cart()

    cart_page.assert_loaded()
    cart_page.assert_item_present(product)
    
    # Remove from cart page
    cart_page.remove_item(product)
    cart_page.assert_items_count(0)

@allure.feature("Cart Management")
@allure.story("Reset App State")
def test_reset_app_state_clears_cart(page):
    """
    Test case to verify that Reset App State clears the cart.
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.assert_loaded()

    home_page.add_to_cart("Sauce Labs Backpack")
    home_page.assert_cart_badge(1)

    home_page.reset_app_state()
    home_page.assert_cart_badge_hidden()
