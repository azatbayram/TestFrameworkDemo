import pytest
import softest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResultsPage
from utilities.utils import Utils
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlights(softest.TestCase):
    log=Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launchpage=LaunchPage(self.driver, self.wait)

    @data(("New Delhi", "New York", "22/02/2023"))
    @unpack
    def test_seach_fights(self, goingFrom, goingTo, date):
        self.launchpage.searchFlights(goingFrom, goingTo, date)
        self.log.warning("Send info successfully")


