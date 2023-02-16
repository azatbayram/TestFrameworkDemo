import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    request.cls.driver=driver
    request.cls.wait=wait

    yield
    time.sleep(3)
    driver.quit()