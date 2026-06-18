import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Заполнение формы логина")
    def login(self, email, password):
        from selenium.webdriver.common.by import By
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)