import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class TestSearchFlights():
    def test_seach_fights(self):
        #Launch browser and navigate to website
        #Providing going from location
        # Providing going to location
        #To resolve sync issue
        #Click on search button
