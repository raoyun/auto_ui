import pytest
from selenium.webdriver.common.by import By
from time import sleep
from testcases.pages.basePage import BasePage


class VideoPage(BasePage):

    def __init__(self, index):
        BasePage.__init__(self, index.login.driver)

    # 模块的关键字
    video_text = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[2]/div/div[2]/a/span')
    # 新建的按钮
    add_btn = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[3]/div[1]/div[2]/a/i')
    # 查看的按钮
    see_btn = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[3]/div[2]/div[3]/a/i')
    # 标题
    title_input = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[1]/textarea[1]')
    # 字号
    # 存在的iframe
    pc_title_iframe = (By.TAG_NAME, 'iframe')
    # pc链接标题
    pc_titile_input = (By.XPATH, '/html/body/p[2]')
    # app链接标题
    app_title_input = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[1]/textarea[2]')
    # 选取视频
    video_btn = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[5]/div[2]/div[1]/div/i')
    # 素材库中选取视频
    video_select = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/img')
    # 确认选取视频
    video_selected_ok = (By.XPATH, '//*[@id="item-detail-panel"]/div[7]/div[5]/a')
    # 默认分类
    default_column = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div[1]/div')
    # 分类右边的展开按钮
    right_open = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div[1]/i')
    # 分类搜索框
    search_input = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/input')
    # 搜索结果的第一条
    search_res_first = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/span')
    # 同时发布到
    # 推荐
    # 发布到pc站
    # 发布到客户端
    # 发布到手机站
    # 视频类型
    # 缩略图
    click_little_photo = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/section/div[1]/div[1]')
    # 素材库选择图片
    library_photo = (By.XPATH, '//*[@id="attachment-list"]/div[19]/div[1]')
    # 选取
    select_photo = (By.XPATH, '//*[@id="attachment-list"]/div[27]/div[3]/div[3]/div[3]/div[2]')
    # 默认
    # 三图
    # 16:9大图
    # 3:1大图
    # 摘要
    Abstract_input = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[4]/textarea')
    # 关键词
    keyword_input = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[1]/div[5]/div/div/div[2]/input')
    # 关联专辑
    # 原创声明
    # 来源名称
    # 来源url
    # 作者
    # 编辑
    # 内容属性
    # 定时上线
    # 定时下线
    # 初始阅读量
    # 开启评论
    # 初始点赞量
    # 发布按钮
    commit_btn = (By.XPATH, '//*[@id="ng-app:cloud-module"]/div[1]/div[1]/div/div[4]/div/div[2]/div[3]/a[1]')


    # 模块关键字
    def text_module_key(self):
        return self.find_element(*self.video_text)

    # 点击添加按钮
    def click_add_btn(self):
        self.click(*self.add_btn)

    # 输入标题
    def input_title(self, text):
        self.type_text(text, *self.title_input)

    # 找到iframe并切换进去
    def switch_pc_title_iframe(self):
        self.switch_frame(*self.pc_title_iframe)

    # 输入pc标题
    def input_pc_title(self, text):
        self.type_text(text, *self.pc_titile_input)

    # 退出iframe
    def pc_title_back_frame(self):
        self.back_frame()

    # 输入app标题
    def input_app_title(self, text):
        self.type_text(text, *self.app_title_input)

    # 点击视频，跳转到素材库
    def click_video(self):
        self.click(*self.video_btn)

    # 点击素材库中的视频
    def click_video_select(self):
        self.click(*self.video_select)

    # 确认素材库中的视频
    def click_video_selected(self):
        self.click(*self.video_selected_ok)

    # 得到默认分类的信息
    def get_default_text(self):
        text = self.get_text(*self.default_column)
        return text

    # 展开分类
    def click_open_column(self):
        self.click(*self.right_open)

    # 输入分类信息
    def input_column_mes(self, text):
        self.type_text(text, *self.search_input)

    # 点击分类信息
    def click_column_mes(self):
        self.click(*self.search_res_first)

    # 点击上传封面
    def click_photo(self):
        self.click(*self.click_little_photo)

    # 点击素材库中的图片
    def click_library_photo(self):
        self.click(*self.library_photo)

    # 点击确认素材库中的图片
    def click_select_photo(self):
        self.click(*self.select_photo)

    # 输入摘要
    def input_abstract(self, text):
        self.type_text(text, *self.Abstract_input)

    # 输入关键字
    def input_keyword(self, text):
        self.type_text(text, *self.keyword_input)

    # 点击发布
    def click_commit_btn(self):
        self.click(*self.commit_btn)










