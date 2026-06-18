from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//a[contains(@class,'BurgerIngredient')]")
    INGREDIENT_DETAIL_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal')]")
    INGREDIENT_DETAIL_CLOSE = (By.XPATH, "//div[contains(@class,'Modal_modal')]//button")
    BUN_SECTION = (By.XPATH, "//section[contains(@class,'BurgerConstructor')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class,'BurgerIngredient')]//p[contains(@class,'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    