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
        print('IM VideoCall setup')
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

    def test_1videocall(self):
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(3)
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
        username=conf.get ("单人聊天", "单人聊天用户")
        self.driver.find_element_by_name(username).click()#进入和某人的IM聊天界面
        time.sleep(5)
        self.driver.find_element_by_id(conf.get("单人聊天","加号更多")).click()#点击加号图标 
        self.driver.find_element_by_id (conf.get("单人聊天", "视频通话")).click()#点击音频通话图标
        time.sleep(3)
        el_hangup=debug_id_pre+'hangup'
        ele = self.driver.find_element_by_android_uiautomator('resourceId("'+el_hangup+'")')
        self.commonCls.result_handler(self.driver,'exsit',ele,'未进入通话界面')
    def test_2b_call_statistics(self):
        time.sleep(3)
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
        self.driver.find_element_by_id(conf.get ("通话统计", "通话统计")).click()#点击通话统计图标
        # source = self.driver.page_source
        time.sleep(2)
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
    def test_3hang_up(self):#挂断通话
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(1)
        self.driver.find_element_by_id(self.commonCls.get_conf("dialPlate","left_btn")).click()
        time.sleep(1)
        self.commonCls.hang_up(self.driver)
        time.sleep(3)
        ele_radio_more = debug_id_pre+'radio_more'
        ele = self.driver.find_element_by_android_uiautomator('resourceId("'+ele_radio_more+'")')
        self.commonCls.result_handler(self.driver,'exsit',ele,'通话界面未关闭')
        self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()


