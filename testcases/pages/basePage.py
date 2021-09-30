from selenium.webdriver import ActionChains
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def type_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.find_element(*loc).click()

    # def double_click(self, *loc):
    #     btn = self.find_element(*loc)
    #     ActionChains(self.driver).double_click(btn).perform()

    def clear(self, *loc):
        self.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title

    def switch_frame(self, *loc):
        iframe = self.driver.find_element(*loc)
        self.driver.switch_to.frame(iframe)

    def back_frame(self):
        self.driver.switch_to.default_content()

    # 得到dom节点的文本信息
    def get_text(self, *loc):
        return self.driver.find_element(*loc).text
