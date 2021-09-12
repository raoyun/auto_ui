from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.rect)
        print(e.size)
        print(e.text)

    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))

        sleep(2)
        e.clear()

    def test_webelement_method2(self):
        from_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        from_element.find_element_by_id('t1').send_keys('haha')



if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_webelement_method2()