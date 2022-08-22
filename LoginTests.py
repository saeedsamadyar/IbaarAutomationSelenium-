from selenium import webdriver
#from webdriver.chrome import ChromeDriverManager
from time import sleep
from Login import Login

driver = webdriver.Chrome(executable_path="/home/myubunto/Downloads/chromedriver_linux64/chromedriver")
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(3)

login: Login = Login(driver=driver)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_on_login_button()
sleep(3)
