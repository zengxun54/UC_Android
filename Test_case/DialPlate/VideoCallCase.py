# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
from Public import commonClass
from lib2to3.tests.support import driver
# from test_mathfunc import TestMathFunc
import HTMLTestRunner
import traceback

class VideoCallCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('VideoCallCase setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
        # return driver
    @classmethod
    def tearDownClass(self):
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.commonCls.restart_adb()
        print('tearDown')
        # self.driver.quit()
    # @unittest.skip("demonstrating skipping")
    def test_1call_num(self):#拨号用例
        call_num_str = '4001'
        result = self.commonCls.call_num(self.driver,call_num_str)
        self.commonCls.result_handler(self.driver,'equal',result,'未进入通话界面')
    def test_2call_statstic(self):
        print('23')
        debug_id_pre = commonClass.debug_id_pre
        self.driver.find_element_by_id(self.commonCls.get_conf("dialPlate","time_container")).click()
        # self.driver.find_element_by_id(debug_id_pre+'time_container').click()
        time.sleep(1)
        # 判断发送分辨率或帧率是否为0
        result = self.commonCls.get_resolution_and_fps(self.driver)
        self.commonCls.result_handler(self.driver,'equal',result,'发送分辨率或帧率为0')
        self.driver.find_element_by_name('接收').click()
        # black_screen_resv = self.commonCls.get_resolution_and_fps(self.driver)
        result = self.commonCls.get_resolution_and_fps(self.driver)
        self.commonCls.result_handler(self.driver,'equal',result,'接收分辨率或帧率为0')
    def test_3hang_up(self):#挂断通话
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(1)
        self.driver.find_element_by_id(self.commonCls.get_conf("dialPlate","left_btn")).click()
        time.sleep(1)
        self.commonCls.hang_up(self.driver)
        time.sleep(3)
        ele = self.driver.find_element_by_android_uiautomator("text(\"拨号\")")
        self.commonCls.result_handler(self.driver,'exsit',ele,'通话界面未关闭')
        self.driver.quit()
# if __name__ == '__main__':
#     unittest.main(verbosity=2)