from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.support.select import Select


class Testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms3.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id('provinces')
        select = Select(se)
        # sleep(2)
        # select.select_by_index(3)
        #
        # sleep(2)
        # select.select_by_value('sh')
        #
        # sleep(2)
        # select.select_by_visible_text('广州')
        #
        # sleep(2)

        # for i in range(4):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(2)
        #
        # select.deselect_all()
        #
        # sleep(2)

        for option in select.options:
            print(option.text)

        self.driver.quit()

if __name__ == '__main__':
    case = Testcase()
    case.test_select()