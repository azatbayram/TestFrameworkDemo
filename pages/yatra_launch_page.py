import logging

from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from utilities.utils import Utils

class LaunchPage(BaseDriver):

    log=Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver=driver
        self.wait=wait

    #Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.driver.find_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departLocation):
        self.getDepartFromField().click()
        self.log.info("Click on going from")
        time.sleep(2)
        self.getDepartFromField().send_keys(departLocation)
        self.log.info("Send departure location")
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("Click on going to")
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("Send going to location")
        time.sleep(2)
        search_results = self.getGoingToResults()
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getDepatureDateField().click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()



