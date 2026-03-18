import allure
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

@allure.feature("Product Sorting")
def test_sort_name_az(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.sort_by("az")
    
    names = home_page.get_all_product_names()
    assert names == sorted(names), f"Products are not sorted A-Z: {names}"

@allure.feature("Product Sorting")
def test_sort_name_za(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.sort_by("za")
    
    names = home_page.get_all_product_names()
    assert names == sorted(names, reverse=True), f"Products are not sorted Z-A: {names}"

@allure.feature("Product Sorting")
def test_sort_price_lohi(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.sort_by("lohi")
    
    prices = home_page.get_all_product_prices()
    assert prices == sorted(prices), f"Prices are not sorted Low to High: {prices}"

@allure.feature("Product Sorting")
def test_sort_price_hilo(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("standard_user", "secret_sauce")
    home_page.sort_by("hilo")
    
    prices = home_page.get_all_product_prices()
    assert prices == sorted(prices, reverse=True), f"Prices are not sorted High to Low: {prices}"
