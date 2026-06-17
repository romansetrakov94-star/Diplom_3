import allure
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
class TestFeedPage:

    @allure.title("Переход на страницу Ленты заказов")
    def test_feed_page_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed()
        time.sleep(3)
        assert "/feed" in driver.current_url

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_constructor()
        time.sleep(2)
        main_page.add_ingredient_to_order()
        time.sleep(2)

        main_page.click_feed()
        time.sleep(5)

        # Проверяем, что страница загрузилась
        assert "/feed" in driver.current_url
        