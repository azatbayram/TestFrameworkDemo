import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResultsPage

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
        launchpage.selectDate("21/02/2023")
        launchpage.clickSearch()
        launchpage.scrollPage()
        #searchpage=SearchFlightResultsPage(self.driver, self.wait)
        #searchpage.filter_flights_by_stop("1 Stop")

