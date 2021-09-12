from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        # id是唯一的
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))

        self.driver.find_element_by_id('su').click()
        sleep(3)
        # self.driver.quit()

    def test_name(self):
        #find_element_by_name() 可能返回多个元素，返回第一个
        #find_elements_by_name() 返回一个集合
        self.driver.find_element_by_name('wd').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)
        self.driver.quit()

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)
        self.driver.quit()

    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_tag(self):
        input = self.driver.find_element_by_tag_name('input')[0]
        print(input)

    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_all(self):
        self.driver.find_element(By.ID,value='kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_linktext()
    # case.test_partial_link_text()
    # case.test_xpath()
    # case.test_tag()
    # case.test_css_selector()
    # case.test_class_name()
    case.test_all()