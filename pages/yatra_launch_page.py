from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LaunchPage():
    def __init__(self, driver):
        self.driver=driver

    def departFrom(self, departLocation):
        depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.clear()
        depart_from.send_keys(departLocation)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)

    def goingTo(self, goingtoLocation):
        going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(2)
        going_to.send_keys(goingtoLocation)

        result_list = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div/li")

        for result in result_list:
            # print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break

    def selectDate(self, departureDate):
        depart_date = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
        depart_date.click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
        date_list = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td")

        # Select departure date
        for date in date_list:
            if date.get_attribute("data-date") == departureDate:
                date.click()
                break

    def clickSearch(self):
        search_button = self.driver.find_element(By.XPATH, "//input[@value='Search Flights']")
        search_button.click()
