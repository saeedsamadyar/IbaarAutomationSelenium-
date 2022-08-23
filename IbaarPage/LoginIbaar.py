class Login:
    def __init__(self, driver):
        self.username_textbox_xpath = "//div[contains(@class,'jss1778 jss1763')]//input"
        self.password_textbox_xpath = "(//div[contains(@class,'jss1778 jss1763')]//input)[2]"
        self.submit_button_xpath = "//button[@type='submit']//span"

        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('xpath', self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('xpath', self.password_textbox_xpath).send_keys(password)

    def click_on_login_button(self, login):
        self.driver.find_element('xpath', self.submit_button_xpath).click()
