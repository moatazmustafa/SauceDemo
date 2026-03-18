import allure
import logging
from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    @allure.step("Assert login page loaded")
    def assert_loaded(self):
        with allure.step("Assert login page loaded"):
            log.info("Assert login page loaded")
            expect(self.login_button).to_be_visible()
            expect(self.username).to_be_visible()

    @allure.step("Login with user")
    def login(self, username: str, password: str):
        with allure.step(f"Login with user:{username}"):
            log.info(f"Login with user:{username}")
            self.username.fill(username)
            self.password.fill(password)
            self.login_button.click()

    @allure.step("Assert login error is visible")
    def assert_error_visible(self):
        with allure.step("Assert login error is visible"):
            log.info("Assert login error is visible")
            expect(self.error).to_be_visible()

    @allure.step("Assert login error message contains: {text}")
    def assert_error_message_contains(self, text: str):
        with allure.step(f"Assert login error message contains: {text}"):
            log.info(f"Assert login error message contains: {text}")
            expect(self.error).to_contain_text(text)