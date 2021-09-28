
import pytest

from testcases.pages.adminLoginPage import AdminLoginPage
from selenium import webdriver
from time import sleep

class TestAdminLogin(object):

    login_data = [
        ('admin@cmstop.com', '123456@cmstop.cn', 'CmsTop媒体云1')
    ]

    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.loginPage = AdminLoginPage(self.driver)
        self.loginPage.goto_login_page()
        # return self.driver

    # 测试用户登录
    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username, pwd, expected', login_data)
    def test_admin_login(self, username, pwd, expected):

        # 输入用户名
        self.loginPage.input_username(username)
        # 输入密码
        self.loginPage.input_pwd(pwd)
        # 点击登录
        self.loginPage.click_login_btn()

        sleep(3)

        # 断言
        assert self.driver.title == expected



if __name__ == '__main__':
    pytest.main(['-sv', 'testAdminLogin.py'])