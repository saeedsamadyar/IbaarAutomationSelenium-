class Login:
    def __init__(self, driver):
        self.submit_button_id = "(//span[@class='jss1340'])[2]"
        self.password_textbox_id = "ibaar_front_password"
        self.username_textbox_id = "ibaar_front_username"

        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', self.password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('xpath', self.submit_button_id).click()
