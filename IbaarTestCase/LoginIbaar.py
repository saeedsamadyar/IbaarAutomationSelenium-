import login as login
from selenium import webdriver
# from webdriver.chrome import ChromeDriverManager
from Pages.Login import Login

driver = webdriver.Chrome(executable_path="/home/myubunto/Downloads/chromedriver_linux64/chromedriver")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://front.ibaar.ir/login/")
driver.implicitly_wait(1)

Login = Login(driver=driver)
# main_page = MainPage(driver=driver)

login.enter_username()
login.enter_password()
login.click_on_login_button()
# sleep(3)
