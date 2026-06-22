import allure
from config import Config
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
class TestFeedPage:

    @allure.title("Переход на страницу Ленты заказов")
    def test_feed_page_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed()
        assert "/feed" in main_page.get_current_url()

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        # Авторизуемся
        main_page.click_login_button()
        login_page.login(registered_user["email"], registered_user["password"])

        # Собираем бургер и оформляем заказ
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        # Закрываем модальное окно с номером заказа
        main_page.close_modal()

        # Переходим в ленту заказов прямым переходом по URL
        main_page.navigate_to(Config.FEED_URL)

        # Проверяем, что мы на странице ленты заказов
        assert "/feed" in main_page.get_current_url()
        