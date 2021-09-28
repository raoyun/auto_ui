from selenium.webdriver.common.by import By
from time import sleep
from testcases.pages.basePage import BasePage


class IndexPage(BasePage):
    def __init__(self, login):
        BasePage.__init__(self, login.driver)

    video_icon = (By.XPATH, '//*[@id="4"]/div[1]/div[2]')

    # 点击视频图标，进入视频模块
    def click_video_icon(self):
        self.click(*self.video_icon)
        sleep(1)

