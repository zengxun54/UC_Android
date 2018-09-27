# -*- encoding:utf-8 -*-

import unittest
from appium import webdriver
import os
import time
import configparser
from Public import commonClass
class CreateDiscussion (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('CreateDiscussion setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    def tearDown(self):
        pass
    def  test_creatediscussion(self):
        time.sleep (5)
        conf = configparser.ConfigParser ()
        conf.read ("../config/parameters.ini", encoding='utf-8')
        abc='tj'
        print('click 1')
        # self.driver.find_element_by_id('action_search').click()  # 进入和某人的IM聊天界面
        self.driver.find_element_by_name('林美霞').click()  # 进入和某人的IM聊天界面
        time.sleep(5)
        self.driver.find_element_by_id(conf.get ("单人聊天", "会话设置")).click()#点击右上角的会话设置图标
        time.sleep (3)
        self.driver.find_element_by_id(conf.get("单人聊天", "添加联系人")).click()#点击添加联系人图标
        time.sleep (3)
        self.driver.find_element_by_id(conf.get("主面板", "选人搜索栏")).send_keys(abc)
        time.sleep (3)
        self.driver.find_element_by_name('汤葭').click ()
        time.sleep (5)
        self.driver.find_element_by_id (conf.get("单人聊天", "创建按钮")).click ()
        time.sleep (5)
        # source = self.driver.page_source
        name1=self.driver.find_element_by_name(u'讨论组创建成功！').text
        name2=self.driver.find_element_by_name(u'您邀请林美霞、汤葭加入本讨论组').text
        try:
            self.assertEqual (name1, u'讨论组创建成功！')
            self.assertEqual (name2, u'您邀请林美霞、汤葭加入本讨论组')
        except Exception as msg:
            # print()
            raise("讨论组创建失败！")
    def  test_creatediscussion_wait(self):
        time.sleep(60)
# if __name__== '__main__':
#     unittest.main ()