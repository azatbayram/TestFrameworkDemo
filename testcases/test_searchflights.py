import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class TestSearchFlights():
    def test_seach_fights(self):
        #Launch browser and navigate to website
        #Providing going from location
        # Providing going to location
        #To resolve sync issue
        #Click on search button
        launchpage=LaunchPage(self.driver, self.wait)
        launchpage.departFrom("New Delhi")
        launchpage.goingTo("New York")
        launchpage.selectDate("19/02/2023")
        launchpage.clickSearch()

