from selenium.webdriver.common.by import By


class FeedPageLocators:
    TOTAL_COUNTER = (By.XPATH, "//div[contains(@class,'OrderFeed')]//p[contains(@class,'digits-large')]")
    TODAY_COUNTER = (By.XPATH, "//div[contains(@class,'OrderFeed')]//p[contains(@class,'digits-large')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed')]/li[1]")
    