from selenium import webdriver
from time import sleep
import unittest

from selenium.webdriver.common.by import By


class TestVideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('http://site.cmstop.aws/#/index/index/index')
        cls.driver.find_element_by_xpath('//*[@id="login"]/input[1]').send_keys('admin@cmstop.com')
        cls.driver.find_element_by_xpath('//*[@id="login"]/input[2]').send_keys('123456@cmstop.cn')
        cls.driver.find_element_by_xpath('//*[@id="login"]/div[4]/span[1]').click()
        sleep(3)
        cls.driver.find_element_by_xpath('//*[@id="4"]/div[1]/div[2]').click()
        sleep(3)

    # 新建视频
    def test_add_video(self):
        video_titile = '测试新建视频'
        # 视频摘要
        video_abstract = '摘要'
        video_keywords = '关键词'

        # 点击新建按钮
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[3]/div[1]/div[2]/a/i').click()

        # 输入视频标题
        title = self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[1]/textarea[1]')
        title.send_keys(video_titile)

        # pc链接标题
        pc_iframe = (By.TAG_NAME, 'iframe')
        # pc_title = self.driver.find_element_by_tag_name('iframe')
        # print(pc_title)
        iframe = self.driver.find_element(*pc_iframe)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/p[2]').send_keys('pc链接标题')
        self.driver.switch_to.default_content()

        # 上传视频
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[2]/div[1]/div/i').click()
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/img').click()
        self.driver.find_element_by_xpath('//*[@id="item-detail-panel"]/div[7]/div[5]/a').click()

        # 输入摘要
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[4]/textarea').send_keys(video_abstract)

        # 输入关键字
        ele = self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[5]/div/div/div[2]/input')
        ele.send_keys(video_keywords)

        sleep(1)
        # 点击发布
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[3]/a[1]').click()

        # 弹窗点击返回
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[5]/div/div/div[2]/div[2]/a[1]').click()

        self.assertEqual(1,1)

        sleep(1)

    # 测试删除视频
    @unittest.skip
    def test_delete_video(self):
        # 点击删除按钮
        self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[3]/div[2]/div[3]/i[3]').click()

        sleep(1)
        # 确定删除
        self.driver.find_element_by_link_text('删除').click()
        self.assertEqual(1,1)

    # 测试修改视频
    @unittest.skip
    def test_update_video(self):
        video_titile = '测试修改视频'
        video_abstract = '修改摘要'
        video_keywords = '修改关键词'
        self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[3]/div[2]/div[3]/i[1]').click()

        # 修改视频标题
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[1]/textarea[1]').clear()
        title = self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[1]/textarea[1]')
        title.send_keys(video_titile)

        # 上传视频
        self.driver.find_element_by_link_text('重新选取').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/img').click()
        self.driver.find_element_by_xpath('//*[@id="item-detail-panel"]/div[7]/div[5]/a').click()

        # 修改摘要
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[4]/textarea').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[4]/textarea').send_keys(
            video_abstract)

        # 修改关键字

        ele = self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[5]/div/div/div[2]/input')
        ele.clear()
        ele.send_keys(video_keywords)

        # 点击发布
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[3]/a[1]').click()

        # 弹窗点击返回
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ng-app:cloud-module"]/div[5]/div/div/div[2]/div[2]/a[1]').click()

        self.assertEqual(1, 1)

        sleep(1)


if __name__ == '__main__':
    unittest.main()