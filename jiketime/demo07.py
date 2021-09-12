from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.support.select import Select


class Testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        # confirm.accept()
        sleep(2)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        sleep(4)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        prompt.accept()
        sleep(3)

if __name__ == '__main__':
    case = Testcase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()
