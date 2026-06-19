import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    @allure.step("Получение счётчика 'Выполнено за всё время'")
    def get_total_counter(self):
        return self.get_text(FeedPageLocators.TOTAL_COUNTER)

    @allure.step("Получение счётчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        return self.get_text(FeedPageLocators.TODAY_COUNTER)

    @allure.step("Получение номера заказа в разделе 'В работе'")
    def get_order_in_progress(self):
        return self.get_text(FeedPageLocators.ORDER_IN_PROGRESS)
    