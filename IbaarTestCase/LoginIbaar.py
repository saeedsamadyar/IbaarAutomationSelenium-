from lib2to3.pgen2 import driver

import login as login
from selenium import webdriver
# from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service
from Pages.Login import Login
from selenium.webdriver.common.keys import keys


driver = webdriver.Chrome(executable_path="/home/myubunto/Downloads/chromedriver_linux64/chromedriver")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://front.ibaar.ir/login")

driver.implicitly_wait(3)

Login = Login(driver=driver)
# main_page = MainPage(driver=driver)


login.enter_username()
login.enter_password()
login.click_on_login_button()
# sleep(3)
