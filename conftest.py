import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config


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