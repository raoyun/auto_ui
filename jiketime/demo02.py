from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()
        sleep(3)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()

        self.driver.close()     #关闭浏览器当前tab
        self.driver.quit()      #关闭当前浏览器

    def test_windows(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to_window(w)
                sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_windows()