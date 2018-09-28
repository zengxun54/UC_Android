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

class callRecordDetailCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.call_num_str = '4001'
        self.call_type = '[视频通话]'
        print('callRecordDetailCase setup')
        desired_cups = {}
        # print('setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('tearDown')
    def test_1call_num(self):
        call_num_str = self.call_num_str
        result = self.commonCls.call_num(self.driver,call_num_str)
        self.commonCls.result_handler(result,"未进入通话界面")
    def test_2hang_up(self):#记录通话类型并挂断通话
        self.driver.find_element_by_id(self.commonCls.debug_id_pre+'name').click()#
        time.sleep(1)
        # com.yealink.uc.android.alpha:id/overlayMenu
        overlayMenu = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'overlayMenu')
        # android.widget.ToggleButton
        type_btn = overlayMenu.find_elements_by_class_name('android.widget.ToggleButton')[1]
        button_type = type_btn.get_attribute('text')
        print(button_type)
        if button_type == '扬声器':
            self.call_type = '[音频通话]'
        time.sleep(1)
        self.commonCls.hang_up(self.driver)
        time.sleep(2)
        iv_call_send = (self.commonCls.debug_id_pre+'tv_recent_calllog_title')
        source = self.driver.page_source
        try:
            assert iv_call_send in source
        except Exception as msg:
            # print('未进入通话界面！')
            raise ('通话界面未挂断')
    def test_3getin_call_record_detail(self):#进入通话记录详情页
        print('test_getin_call_record_detail')
        source = self.driver.page_source
        debug_id_pre = commonClass.debug_id_pre
        el = debug_id_pre+'iv_call_send'
        # 拨号界面如果有拨号键，再次点击拨号页签按钮
        if el in source:
            iv_call_send = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tab_text')[2].click()
            time.sleep(1)
        time.sleep(3)
        lv_contact_log = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'lv_contact_log')
        print(lv_contact_log)
        calllog_set = lv_contact_log.find_elements_by_class_name("android.widget.RelativeLayout")
        #点击第一条通话记录
        calllog_set[1].find_element_by_id(self.commonCls.debug_id_pre+'call_log_info').click()
    #     com.yealink.uc.android.alpha:id/title
        time.sleep(3)
        detail_el = debug_id_pre+'tv_recent_calllog_title'
        detail_source = self.driver.page_source
        try:
            assert detail_el not in detail_source
        except Exception as msg:
            print('未进入通话记录详情界面！')
            raise ('未进入通话记录详情界面！')
    def test_4detail_title(self):#检查通话记录详情标题
        print('test_detail_title')
        # com.yealink.uc.android.alpha:id/title
        detail_title_ele = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'title')
        detail_title = detail_title_ele.get_attribute('text')
        print('detail_title')
        print(detail_title)
        try:
            assert detail_title == '通话详情'
        except Exception as msg:
            print('通话详情页标题未显示！')
            raise ('通话详情页标题未显示！')
    def test_5detail_call_type(self):#检查通话记录详情最后一路通话的通话类型
        print('test_detail_call_type')
        # com.yealink.uc.android.alpha:id/title
        # com.yealink.uc.android.alpha:id/tv_call_protocol
        detail_calltype_ele = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tv_call_protocol')
        detail_call_type = detail_calltype_ele[0].get_attribute('text')
        print('detail_call_type')
        print(detail_call_type)
        try:
            assert detail_call_type == self.call_type
        except Exception as msg:
            print('通话详情页的通话类型与实际通话类型不符')
            raise ('通话详情页的通话类型与实际通话类型不符！')
    def test_6detail_call_num(self):#检查通话记录详情的号码
        print('test_detail_call_num')
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        # 滑动屏幕--上滑
        self.driver.swipe(width*0.5, height*0.75, width*0.5, height*0.25, 2000)
        # com.yealink.uc.android.alpha:id/title
        # com.yealink.uc.android.alpha:id/tv_call_protocol
        time.sleep(5)
        detail_callnum_ele = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'item_contact_detail_subtitle')
        detail_call_num = detail_callnum_ele.get_attribute('text')
        print(detail_call_num)
        try:
            assert detail_call_num == self.call_num_str
        except Exception as msg:
            print('通话详情页的通话号码与实际通话号码不符')
            raise ('通话详情页的通话号码与实际通话号码不符！')
    def test_7wait(self):
        time.sleep(60)
# if __name__== '__main__':
#     unittest.main(verbosity=2)
#     suite = unittest.TestSuite()
#     # 将测试用例加入到测试容器中
#     print(suite)
#     suite.addTests([callRecordDetailCase('test_1call_num'),callRecordDetailCase('test_2hang_up'),callRecordDetailCase('test_3getin_call_record_detail'),callRecordDetailCase('test_4detail_title'),callRecordDetailCase('test_5detail_call_type'),callRecordDetailCase('test_6detail_call_num')])
#     report_path = r'E:\testresult.html'
#     fp = open(report_path, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
#     runner.run(suite)
#     print('123')
#     fp.close()