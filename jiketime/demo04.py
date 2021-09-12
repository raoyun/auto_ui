from selenium import webdriver
import os
from time import sleep

class Testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms.html'
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('ry')
        password = self.driver.find_element_by_id('pwd')
        password.send_keys('ry')

        print(username.get_attribute('value'))
        print(password.get_attribute('value'))

        sleep(2)
        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()

        username.clear()
        password.clear()

if __name__ == '__main__':
    case = Testcase()
    case.test_login()