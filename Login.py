class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "UserName"
        self.password_textbox_xpath = "//button[@class='btn btn-success']"
        self.login_button_xpath = "//button[@class='btn btn-success']"

        def enter_username(self, username):
            self.driver.find('id', self.username_textbox_id).send_keys(username)

        def enter_password(self, password):
            self.driver.find('xpath', self.password_textbox_xpath)

        def click_on_login_button(self):
                self.driver.find('xpath', self.login_button_xpath).click()



