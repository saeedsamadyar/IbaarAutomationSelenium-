class Login:
    def __init__(self, driver):
        self.username_textbox_xpath = "//input[contains(@class,'jss1789 jss1773')]"
        self.password_textbox_xpath = "(//input[contains(@class,'jss1789 jss1773')])[2]"
        self.submit_button_xpath = "(//span[@class='jss1650'])[2]"
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('xpath', self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('xpath', self.password_textbox_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath', self.submit_button_xpath).click()
