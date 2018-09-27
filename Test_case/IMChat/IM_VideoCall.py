# -*- encoding:utf-8 -*-

import unittest
from appium import webdriver
import os
import time
import configparser
from Public import commonClass
class VideoCall (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('VideoCall setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
    @classmethod
    def tearDownClass(self):
        pass
        # self.driver.find_element_by_id ('com.yealink.uc.android:id/left_btn').click ()#点击左上角的X图标
        # # self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/iconEncrypt').click()#点击顶部盾牌图标
        # self.driver.find_element_by_id ('com.yealink.uc.android:id/hangup').click ()  # 挂断通话
        # # time.sleep (2)
        # # self.driver.find_element_by_id ('com.yealink.uc.android.alpha:id/btnCancel').click ()  # 结束会议

    def test_audiocall(self):
        time.sleep(3)
        conf = configparser.ConfigParser ()
        conf.read ("../config/parameters.ini", encoding='utf-8')
        username=conf.get ("单人聊天", "单人聊天用户")
        self.driver.find_element_by_name(username).click()#进入和某人的IM聊天界面
        time.sleep (5)
        self.driver.find_element_by_id(conf.get("单人聊天","加号更多")).click()#点击加号图标 
        self.driver.find_element_by_id (conf.get("单人聊天", "视频通话")).click()#点击音频通话图标
        time.sleep(10)
        source = self.driver.page_source
        print (source)
        el = 'com.yealink.uc.android:id/name'
        try:
            assert el in source
        except Exception as msg:
            print ('未进入通话界面！')
            raise
    def test_b_call_statistics(self):
        time.sleep(3)
        conf = configparser.ConfigParser ()
        conf.read ("../config/parameters.ini", encoding='utf-8')
        self.driver.find_element_by_id(conf.get ("通话统计", "通话统计")).click()#点击通话统计图标
        source = self.driver.page_source
        signal_send = self.driver.find_element_by_id(conf.get ("通话统计", "发送数据")).text
        codec1 = self.driver.find_element_by_id (conf.get ("通话统计", "编解码格式")).text
        self.driver.find_element_by_name('接收').click()
        signal_rec = self.driver.find_element_by_id (conf.get ("通话统计", "接收数据")).text
        codec2=self.driver.find_element_by_id(conf.get ("通话统计", "编解码格式")).text
        try:
            self.assertNotEqual(signal_send, u'0*0')
            self.assertNotEqual (signal_rec, u'0*0')
            self.assertNotEqual(codec1,u'H.264 High Profile')
            self.assertNotEqual (codec2, u'H.264 High Profile')
        except Exception as msg:
            print ('通话数据异常！')
            raise
    def  test_video_call_wait(self):
        time.sleep(60)
# if __name__== '__main__':
#     unittest.main ()


