# -*- encoding:utf-8 -*-

import unittest
import time
import os
import configparser
from appium import  webdriver
from Public import commonClass
class SendMsg (unittest.TestCase):
    # @classmethod
    def setUpClass(self):
        print('SendMsg setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
    # @classmethod
    def tearDownClass(self):
        pass
        # self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()#返回最近会话列表

    def test_sendimage(self):
        time.sleep(20)
        print('test_sendimage')
        conf = configparser.ConfigParser()
        conf.read (commonClass.param_url,encoding='utf-8')
        username=conf.get ("单人聊天", "单人聊天用户")
        self.driver.find_element_by_name(username).click ()  # 进入和某人的IM聊天界面
        time.sleep(5)
        self.driver.find_element_by_id(conf.get ("单人聊天", "表情")).click()#点击表情图标
        time.sleep (2)
        self.driver.find_element_by_xpath (conf.get ("单人聊天", "笑脸")).click()#点击笑脸表情、
        time.sleep (2)
        self.driver.find_element_by_id (conf.get ("单人聊天", "发送")).click ()#点击发送
        name1 = self.driver.find_element_by_id (commonClass.debug_id_pre+'chat_bar_editor').text
        try:
            self.assertEqual (name1, u'')
        except Exception as msg:
            print("表情未发送")
            raise('表情未发送')
    def test_sendmsg(self):
        print('test_sendmsg')
        time.sleep(5)
        conf = configparser.ConfigParser()
        conf.read (commonClass.param_url,encoding='utf-8')
        abc='Test msg'
        username=conf.get ("单人聊天", "单人聊天用户")
        self.driver.find_element_by_name(username).click()#进入和某人的IM聊天界面
        self.driver.find_element_by_id(conf.get ("单人聊天", "文本输入框")).send_keys(abc)#在文本输入框输入需要发送的文本
        self.driver.find_element_by_id (conf.get ("单人聊天", "发送")).click()#点击发送

        name1 = self.driver.find_element_by_id (commonClass.debug_id_pre+'chat_bar_editor').text
        try:
            self.assertEqual (name1, u'')
        except Exception as msg:
            print ("消息未发送")
            raise ('消息未发送')

    def test_status(self):
        print('test_status')
        time.sleep(5)
        source = self.driver.page_source
        status=(commonClass.debug_id_pre+'record_status')
        try:
            assert status  not in source
        except Exception as msg:
            print('发送失败！')
            raise('发送失败！')
#     def test_send_msg_wait(self):
#         time.sleep(60)
# if __name__== '__main__':
#     unittest.main ()


