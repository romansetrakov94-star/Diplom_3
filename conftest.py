import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config
from helpers import register_user_and_return_data, delete_user


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unknown browser: {browser}")

    driver.get(Config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    user = register_user_and_return_data()
    yield user
    if user and user.get("token"):
        delete_user(user["token"])