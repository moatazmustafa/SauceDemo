import allure
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

@allure.feature("Authentication")
@allure.story("Login and Logout")
def test_login_logout(page):
    """
    Test case to verify successful login and logout flow.
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)

    # 1) Login with valid credentials
    login_page.login("standard_user", "secret_sauce")

    # 2) Assert Home page is loaded
    home_page.assert_loaded()

    # 3) Logout
    home_page.logout()

    # 4) Assert redirected to login page
    login_page.assert_loaded()

@allure.feature("Authentication")
@allure.story("Invalid Login")
def test_invalid_login(page):
    """
    Test case to verify error message on invalid login.
    """
    login_page = LoginPage(page)

    # 1) Login with invalid credentials
    login_page.login("invalid_user", "invalid_password")

    # 2) Assert error message is visible
    login_page.assert_error_visible()
