class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "UserName"
        self.password_textbox_id = "Password"
        self.login_button_xpath = "//button[@type='button']"

        def enter_username(self, username):
            self.driver.find_element('xpath', self.username_textbox_id).send_keys(username)

        def enter_password(self, password):
            self.driver.find_element('xpath', self.password_textbox_id).send_keys(password)

        def click_on_login_button(self):
            self.driver.find_element('xpath', self.login_button_xpath).click()












