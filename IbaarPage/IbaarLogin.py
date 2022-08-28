class Login:
    def __init__(self, driver):

        self.submit_button_xpath = "//button[@id='ibaar_login']//span"
        self.password_textbox_xpath = "ibaar_front_password"
        self.username_textbox_xpath = "ibaar_front_username"
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', self.password_textbox_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath', self.submit_button_xpath).click()
