from Locators import *

class Login:
    def __init__(self, driver):
        self.username_textbox_xpath = "//input[@placeholder='Username']"
        self.password_textbox_xpath = "//input[@placeholder='Password']"
        self.submit_button_xpath = "//button[@type='submit']"
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('xpath', self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('xpath', self.password_textbox_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath', self.submit_button_xpath).click()
