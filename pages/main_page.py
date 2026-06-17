import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        time.sleep(3)  # Ждём загрузку

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)
        time.sleep(3)  # Ждём загрузку

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Проверка открытия окна с деталями")
    def is_ingredient_detail_open(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_DETAIL_WINDOW)

    @allure.step("Закрытие окна с деталями")
    def close_ingredient_detail(self):
        time.sleep(1)
        self.click(MainPageLocators.INGREDIENT_DETAIL_CLOSE)
        time.sleep(1)

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        from selenium.webdriver.common.action_chains import ActionChains
        source = self.wait.until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT))
        target = self.wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_SECTION))
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON_MAIN)
        