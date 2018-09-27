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

class callRecordCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        self.first_calllog_type  = '[视频通话]'
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('tearDown')
        #@通话记录回拨
    def test_1calllog_back(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
        time.sleep(1)
        source = self.driver.page_source
        el = ('com.yealink.uc.android.alpha:id/iv_call_send')
        # 拨号界面如果有拨号键，再次点击拨号页签按钮
        if el in source:
            iv_call_send = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tab_text')[2].click()
            time.sleep(1)
        time.sleep(3)
        call_log_none_el = 'com.yealink.uc.android.alpha:id/tv_none'
        try:
            assert call_log_none_el not in source
        except Exception as msg:
            print('没有通话记录！')
            raise ('没有通话记录')
        lv_contact_log = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'lv_contact_log')
        #获取第1个通话记录的通话类型
        self.first_calllog_type = self.commonCls.get_first_calllog_info(self.driver,'call_log_protocol')
        print(self.first_calllog_type)
        #获取通话记录集合
        calllog_set = lv_contact_log.find_elements_by_class_name("android.widget.RelativeLayout")
        calllog_set[1].click()
        print(len(calllog_set))
        time.sleep(3)
        el=('com.yealink.uc.android.alpha:id/name')
        try:
            assert el not in source
        except Exception as msg:
            print('通话记录回拨失败！')
            raise ('未进入通话界面')
    def test_2check_call_type(self):
        debug_id_pre = commonClass.debug_id_pre
        source = self.driver.page_source
        print(self.first_calllog_type)
        el = debug_id_pre+'stopVideo'
        button = '摄像头按钮'
        if self.first_calllog_type == '[音频通话]':
            el = debug_id_pre+'switchSpeaker'
            button = '扬声器按钮'
        self.driver.find_element_by_id(self.commonCls.debug_id_pre+'name').click()#通话界面图标
        try:
            assert el in source
        except Exception as msg:
            print(self.first_calllog_type+'界面没有！'+button)
            raise ('未进入通话界面')
    def test_3hang_up(self):#挂断通话
        self.commonCls.hang_up(self.driver)
        time.sleep(2)
        iv_call_send = (self.commonCls.debug_id_pre+'tv_recent_calllog_title')
        source = self.driver.page_source
        try:
            assert iv_call_send in source
        except Exception as msg:
            # print('未进入通话界面！')
            raise ('通话界面未挂断')
    def test_4wait(self):
        time.sleep(60)
if __name__== '__main__':
    unittest.main(verbosity=2)
    # suite = unittest.TestSuite()
    # # 将测试用例加入到测试容器中
    # # print(suite)
    # # suite.addTests([callRecordCase('test_calllog_back'),callRecordCase('test_hang_up')])
    # suite.addTests([callRecordCase('test_1calllog_back'),callRecordCase('test_2check_call_type'),callRecordCase('test_3hang_up')])
    #
    # report_path = r'E:\testresult.html'
    # fp = open(report_path, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
    # runner.run(suite)
    # print('123')
    # fp.close()