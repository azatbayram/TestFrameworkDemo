import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResultsPage

@pytest.mark.usefixtures("setup")
class TestSearchFlights():
    def test_seach_fights(self):

        launchpage=LaunchPage(self.driver, self.wait)
        launchpage.searchFlights("New Delhi", "New York", "22/02/2023")


