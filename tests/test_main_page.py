import allure
import time
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainPage:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert "/" in main_page.get_current_url()

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_feed_navigation(self, driver):
        main_page = MainPage(driver)
        time.sleep(2)
        main_page.click_feed()
        time.sleep(5)
        assert "/feed" in main_page.get_current_url()

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_detail_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_ingredient_detail_open()

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_ingredient_detail_closes(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredient_detail()
        assert not main_page.is_ingredient_detail_open()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        counter_before = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        counter_after = main_page.get_ingredient_counter()
        assert int(counter_after) > int(counter_before)
        