import pytest
import softest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResultsPage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchFlights(softest.TestCase):
    log=Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launchpage=LaunchPage(self.driver, self.wait)
    def test_seach_fights(self):
        self.launchpage.searchFlights("New Delhi", "New York", "22/02/2023")
        self.log.warning("Send info successfully")


