from selenium.webdriver.common.by import By
from time import sleep
from testcases.pages.basePage import BasePage

class AdminLoginPage(BasePage):

    username_input = (By.NAME, 'username')
    pwd_input = (By.XPATH, '//*[@id="login"]/input[2]')
    login_btn = (By.NAME, 'login')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self):
        self.driver.get('http://site.cmstop.aws/login#/index/index/index')
        self.driver.maximize_window()

    def input_username(self, username):
        self.type_text(username, *self.username_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd, *self.pwd_input)

    def click_login_btn(self):
        self.click(*self.login_btn)
        sleep(1)
