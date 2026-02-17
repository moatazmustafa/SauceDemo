from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from pages.ShippingPage import ShippingPage
from pages.CheckoutPage import CheckoutPage
from pages.SuccessPage import SuccessPage


def test_e2e_two_items_checkout(page):
    # 1) Login
    LoginPage(page).login("standard_user", "secret_sauce")

    # 2) Home assertions
    home = HomePage(page)
    home.assert_loaded()

    # 3) Product 1 -> assert title -> add -> back home
    product1 = "Sauce Labs Backpack"
    home.open_product(product1)

    product = ProductPage(page)
    product.assert_loaded(product1)
    product.add_to_cart()
    product.back_home()

    # 4) Product 2 -> assert title -> add -> back home
    home.assert_loaded()
    product2 = "Sauce Labs Bike Light"
    home.open_product(product2)

    product.assert_loaded(product2)
    product.add_to_cart()
    product.back_home()

    # 5) Go to cart -> assert items
    home.go_to_cart()

    cart = CartPage(page)
    cart.assert_loaded()
    cart.assert_items_count(2)
    cart.assert_item_present(product1)
    cart.assert_item_present(product2)
    cart.checkout()

    # 6) Shipping -> fill -> continue
    shipping = ShippingPage(page)
    shipping.assert_loaded()
    shipping.fill("Moataz", "Mustafa", "2312")
    shipping.continue_to_checkout()

    # 7) Checkout -> assert totals -> finish
    checkout = CheckoutPage(page)
    checkout.assert_loaded()
    checkout.assert_totals("Total: $43.18")  # matches your screenshot for 2 items
    checkout.finish()

    # 8) Complete -> assert success message
    complete = SuccessPage(page)
    complete.assert_loaded()
    complete.assert_success_message()

    # 9) Logout
    home.logout()
