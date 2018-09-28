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

class callBackCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('callBackCase setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        self.first_calllog_type = '[视频通话]'
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('tearDown')
        #@通话记录回拨
    def test_1calllog_back(self):
        print('test_1calllog_back')
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
        time.sleep(1)
        source = self.driver.page_source
        el = (commonClass.debug_id_pre+'iv_call_send')
        # 拨号界面如果有拨号键，再次点击拨号页签按钮
        if el in source:
            iv_call_send = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tab_text')[2].click()
            time.sleep(1)
        time.sleep(3)
        # call_log_none_el = commonClass.debug_id_pre+'tv_none'
        # try:
        #     assert call_log_none_el not in source
        # except Exception as msg:
        #     print('没有通话记录！')
        #     raise ('没有通话记录')
        result = commonClass.debug_id_pre+'tv_none'
        self.commonCls.result_handler(result,'通话记录回拨失败！')
        lv_contact_log = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'lv_contact_log')
        #获取第1个通话记录的通话类型
        self.first_calllog_type = self.commonCls.get_first_calllog_info(self.driver,'call_log_protocol')
        print(self.first_calllog_type)
        #获取通话记录集合
        calllog_set = lv_contact_log.find_elements_by_class_name("android.widget.RelativeLayout")
        calllog_set[1].click()
        print(len(calllog_set))
        time.sleep(3)
        el=(commonClass.debug_id_pre+'name')
        result = el not in source
        self.commonCls.result_handler(result,'通话记录回拨失败！')
    # def test_2check_call_type(self):
        time.sleep(6)
        # self.driver.find_element_by_id(commonClass.debug_id_pre+'name').click()#通话界面图标

        print('test_2check_call_type')
        debug_id_pre = commonClass.debug_id_pre
        self.driver.find_element_by_id(debug_id_pre+'iconEncrypt').click()#判断通话界面图标是否出现
        source = self.driver.page_source
        print(self.first_calllog_type)
        el = debug_id_pre+'stopVideo'
        button = '摄像头按钮'
        if self.first_calllog_type == '[音频通话]':
            el = debug_id_pre+'switchSpeaker'
            button = '扬声器按钮'
        self.driver.find_element_by_id(self.commonCls.debug_id_pre+'iconEncrypt').click()#通话界面图标
        result = el in source
        msg = self.first_calllog_type+'界面没有！'+button
        self.commonCls.result_handler(result,msg)
         # #挂断通话
        print('test_2check_call_type')
        self.commonCls.hang_up(self.driver)
        time.sleep(2)
        iv_call_send = (self.commonCls.debug_id_pre+'tv_recent_calllog_title')
        source = self.driver.page_source
        result = iv_call_send in source
        self.commonCls.result_handler(result,'通话界面未挂断')
# if __name__== '__main__':
#     unittest.main(verbosity=2)
