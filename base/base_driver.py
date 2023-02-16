import time

class BaseDriver():

    def __init__(self, driver):
        self.driver=driver

    def scrollPage(self):
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if (lastCount == pageLength):
                match = True
        time.sleep(4)
