import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Заполнение формы логина")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_FIELD, email)
        self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        