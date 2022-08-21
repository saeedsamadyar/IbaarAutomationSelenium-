from selenium import webdriver
from webdriver.chrome import ChromeDriverManager
from time import sleep
from Login import Login

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://ibaar.ir:8081/account/login?type=payload")
driver.implicitly_wait(3)

login = Login(driver=driver)

login.enter_username("mohammad")
login.enter_password("111111")
login.click_on_login_button()
sleep(3)


