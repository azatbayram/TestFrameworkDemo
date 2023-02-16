import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)