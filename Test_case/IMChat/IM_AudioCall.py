# -*- encoding:utf-8 -*-

import unittest
from appium import webdriver
import os
import time
import configparser
from Public import commonClass
class AudioCall (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('IM AudioCall setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
    @classmethod
    def tearDownClass(self):
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.commonCls.restart_adb()
        print('tearDown')
        # debug_id_pre = commonClass.debug_id_pre
    def test_audiocall(self):
        print('test_audiocall')
        time.sleep(5)
        debug_id_pre = commonClass.debug_id_pre
        conf = configparser.ConfigParser()
        conf.read(commonClass.param_url, encoding='utf-8')
        # username='测试1'
        # username='测试1'
        username=conf.get ("单人聊天", "单人聊天用户")
        print(username)
        print('test username')

        self.driver.find_element_by_name(username).click()#进入和某人的IM聊天界面
        time.sleep(1)
        self.driver.find_element_by_id(conf.get ("单人聊天", "加号更多")).click()#点击加号图标
        time.sleep(1)
        self.driver.find_element_by_id (conf.get ("单人聊天", "音频通话")).click()#点击音频通话图标
        time.sleep(5)
        source = self.driver.page_source
        print (source)
        el=debug_id_pre+'hangup'
        try:
            assert el in source
        except Exception as msg:
            print ('未进入通话界面！')
            raise
    # def test_call_statistics(self):
        print('test_call_statistics')
        debug_id_pre = commonClass.debug_id_pre
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
        self.driver.find_element_by_id(conf.get ("通话统计", "通话统计")).click()#点击通话统计图标
        source = self.driver.page_source
        codec=self.driver.find_element_by_id(conf.get ("通话统计", "编解码格式")).text
        recv_protocol=self.driver.find_element_by_id(conf.get ("通话统计", "通话协议类型")).text
        try:
            self.assertEquals(recv_protocol,u'协议:SIP')
            self.assertEquals(codec,u'opus')

        except Exception as msg:
            print ('通话数据异常！')
            self.driver.find_element_by_id(debug_id_pre+'hangup').click()#点击挂断图标
            raise
        self.driver.find_element_by_id(debug_id_pre+'hangup').click()#点击挂断图标
    # def test_Audio_wait(self):
    #     time.sleep(60)
# if __name__ == '__main__':
#     unittest.main()


