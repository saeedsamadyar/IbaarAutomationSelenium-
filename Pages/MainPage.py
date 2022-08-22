from Locators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_label_xpath = "//div[@role='dialog']/following-sibling::div[1]"

        def check_main_page(self):
            self.driver.find_element('xpath', self.dashboard_label_xpath)
