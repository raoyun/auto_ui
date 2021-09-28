import pytest
from testcases.tests.testAdminLogin import TestAdminLogin
from testcases.pages.indexPage import IndexPage
from time import sleep

class TestIndexPage(object):

    def setup_class(self) -> None:
        self.login = TestAdminLogin()
        self.indexPage = IndexPage(self.login)

    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.dependency(name='index_video')
    def test_click_video_icon(self):
        self.indexPage.click_video_icon()
        sleep(1)

        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-sv', 'testIndex.py'])

