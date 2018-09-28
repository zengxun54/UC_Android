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
    def test_1call_record(self):#通话记录
        print('13')
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
        time.sleep(1)
        source = self.driver.page_source
        el = debug_id_pre+'iv_call_send'
        # 拨号界面如果有拨号键，再次点击拨号页签按钮
        if el in source:
            iv_call_send = self.driver.find_elements_by_id(debug_id_pre+'tab_text')[2].click()
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
        self.commonCls.result_handler(result,"未进入通话界面")
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
    def test_4check_call_record(self):
        source = self.driver.page_source
        debug_id_pre = commonClass.debug_id_pre
        el = debug_id_pre+'iv_call_send'
        # 拨号界面如果有拨号键，再次点击拨号页签按钮
        if el in source:
            iv_call_send = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tab_text')[2].click()
            time.sleep(1)
        time.sleep(3)
        # 通话记录总数---通话记录回拨后
        calllog_all_count_after_callback = self.commonCls.get_calllog_counter(self.driver)
        time.sleep(1)
        #获取第一条通话记录的记录数---通话记录回拨后
        calllog_first_count_after_callback = self.commonCls.get_first_calllog_info(self.driver,'call_log_name')
        print('self.calllog_all_count')
        print(calllog_all_count)
        print('scalllog_all_count_after_callback')
        print(calllog_all_count_after_callback)
        print('calllog_first_count')
        print(calllog_first_count)
        print('calllog_first_count_after_callback')
        print(calllog_first_count_after_callback)
        try:
            assert not (int(calllog_all_count_after_callback) != int(calllog_all_count)+1 and int(calllog_first_count_after_callback) != int(calllog_first_count)+1)
        except Exception as msg:
            # print('未进入通话界面！')
            raise ('通话记录数显示不正确')
    def test_5wait(self):
        time.sleep(60)
# if __name__== '__main__':
#     unittest.main(verbosity=2)
#     suite = unittest.TestSuite()
#     # 将测试用例加入到测试容器中
#     print(suite)
#     suite.addTests([callRecordCase('test_1call_record'),callRecordCase('test_2call_num'),callRecordCase('test_3hang_up'),callRecordCase('test_4check_call_record')])
#     report_path = r'E:\testresult.html'
#     fp = open(report_path, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
#     runner.run(suite)
#     print('123')
#     fp.close()