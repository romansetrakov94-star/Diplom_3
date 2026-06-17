from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # Увеличил с 15 до 30

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка отображения элемента")
    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url