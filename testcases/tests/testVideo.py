import pytest
from testcases.tests.testIndex import TestIndexPage
from testcases.pages.videoPage import VideoPage
from testcases.tests.testAdminLogin import TestAdminLogin
from time import sleep

class TestVideoPage(object):

    video_data = [
        ('标题', 'pc链接标题', 'app链接标题', '摘要', '关键词')
    ]

    def setup_class(self) -> None:
        # TestIndexPage()
        self.index = TestIndexPage()
        self.videoPage = VideoPage(self.index)

    # 验证是否是视频模块
    @pytest.mark.dependency(depends=["index_video"], scope="module")
    def test_video_keyword(self):
        sleep(5)
        module_key = self.videoPage.text_module_key()
        assert module_key.text == '视频'

    # 新建视频
    @pytest.mark.parametrize('title,pc,app,abstract,keyword', video_data)
    @pytest.mark.dependency(depends=["index_video"], scope="module")
    def test_add_video(self, title,pc,app,abstract,keyword):
        self.videoPage.click_add_btn()
        sleep(2)
        self.videoPage.input_title(title)
        self.videoPage.switch_pc_title_iframe()
        self.videoPage.input_pc_title(pc)
        self.videoPage.back_frame()
        self.videoPage.input_app_title(app)
        self.videoPage.click_video()
        sleep(2)
        self.videoPage.click_video_select()
        sleep(1)
        self.videoPage.click_video_selected()
        # self.videoPage.click_photo()
        # self.videoPage.click_library_photo()
        # self.videoPage.click_select_photo()
        self.videoPage.input_abstract(abstract)
        self.videoPage.input_keyword(keyword)
        self.videoPage.click_commit_btn()


    # 删除视频

    # def test_del_video(self):
    #     pass
    #
    #
    # def test_select_video(self):
    #     pass




if __name__ == '__main__':
    pytest.main(['-sv', 'testVideo.py'])

