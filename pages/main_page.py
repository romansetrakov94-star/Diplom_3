import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)
        self.wait.until(EC.url_contains("/feed"))

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Проверка открытия окна с деталями")
    def is_ingredient_detail_open(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_DETAIL_WINDOW)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        close_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT_DETAIL_CLOSE))
        self.driver.execute_script("arguments[0].click();", close_button)
        # Ждём, пока модальное окно и оверлей полностью исчезнут
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAIL_WINDOW))

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BUN_SECTION)
        self.wait_for_element_visible(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON_MAIN)
        