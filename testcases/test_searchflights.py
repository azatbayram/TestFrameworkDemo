import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestSearchFlights():
    def test_seach_fights(self):
        #Launch browser and navigate to website


        #Providing going from location
        depart_from=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.clear()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        # Providing going to location
        going_to=driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")

        result_list=driver.find_elements(By.XPATH, "//div[@class='viewport']//div/li")

        for result in result_list:
            #print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break
        #To resolve sync issue
        depart_date=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
        depart_date.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
        date_list=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td")

        #Select departure date
        for date in date_list:
            if date.get_attribute("data-date")=="17/02/2023":
                date.click()
                break
        time.sleep(3)
        #Click on search button
        search_button=driver.find_element(By.XPATH, "//input[@value='Search Flights']")
        search_button.click()

        time.sleep(3)
        driver.quit()

demoTest=TestSearchFlights
demoTest.test_seach_fights()
