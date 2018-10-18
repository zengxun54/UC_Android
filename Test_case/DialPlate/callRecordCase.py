# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
from Public import commonClass
# from test_mathfunc import TestMathFunc
import HTMLTestRunner
import traceback
import re
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
calllog_all_count = None
calllog_first_count = None
class callRecordCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('callRecordCase setup')
        self.call_num_str = '4001'
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('callRecordCase tearDown')
        # self.driver.quit()
    def test_1call_record(self):#通话记录
        print('13')
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
        time.sleep(1)
        time.sleep(3)
        # 通话记录总数
        global calllog_all_count
        calllog_all_count = self.commonCls.get_calllog_counter(self.driver)
        print('test_1call_record calllog_all_count')
        print(calllog_all_count)
        time.sleep(1)
        #获取第一条通话记录的记录数
        global calllog_first_count
        calllog_first_count = self.commonCls.get_first_calllog_info(self.driver,'call_log_name')
    def test_2call_num(self):
        call_num_str = self.call_num_str
        result = self.commonCls.call_num(self.driver,call_num_str)
        self.commonCls.result_handler(self.driver,'equal',result,'未进入通话界面')
    def test_3hang_up(self):#挂断通话
        self.commonCls.hang_up(self.driver)
        time.sleep(3)
        ele = self.driver.find_element_by_android_uiautomator("text(\"拨号\")")
        self.commonCls.result_handler(self.driver,'exsit',ele,'通话界面未关闭')
    def test_4check_call_record(self):
        time.sleep(2)
        # 通话记录总数---通话记录回拨后
        calllog_all_count_after_callback = self.commonCls.get_calllog_counter(self.driver)
        time.sleep(1)
        #获取第一条通话记录的记录数---通话记录回拨后
        calllog_first_count_after_callback = self.commonCls.get_first_calllog_info(self.driver,'call_log_name')
        result = ((int(calllog_all_count_after_callback) != int(calllog_all_count)+1 and int(calllog_first_count_after_callback) != int(calllog_first_count)+1))
        self.commonCls.result_handler(self.driver,'exsit',result,'通话记录数显示不正确')
        self.driver.quit()
# if __name__== '__main__':
#     unittest.main(verbosity=2)
