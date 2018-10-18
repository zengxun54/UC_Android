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
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('tearDown')
    # def test_1call_num(self):
    #     call_num_str = self.call_num_str
    #     result = self.commonCls.call_num(self.driver,call_num_str)
    #     # self.commonCls.result_handler(self.driver,result,'未进入通话界面！')
    #     self.commonCls.result_handler(self.driver,'equal',result,'未进入通话记录详情界面')
    # def test_2hang_up(self):#记录通话类型并挂断通话
    #     self.driver.find_element_by_id(self.commonCls.debug_id_pre+'nameContainer').click()#
    #     time.sleep(1)
    #     # com.yealink.uc.android.alpha:id/overlayMenu
    #     overlayMenu = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'overlayMenu')
    #     # android.widget.ToggleButton
    #     type_btn = overlayMenu.find_elements_by_class_name('android.widget.ToggleButton')[1]
    #     button_type = type_btn.get_attribute('text')
    #     print(button_type)
    #     if button_type == '扬声器':
    #         self.call_type = '[音频通话]'
    #     time.sleep(1)
    #     self.commonCls.hang_up(self.driver)
    #     time.sleep(5)
    #     ele = self.driver.find_element_by_android_uiautomator("text(\"拨号\")")
    #     self.commonCls.result_handler(self.driver,'exsit',ele,'通话界面未关闭')
    def test_3getin_call_record_detail(self):#进入通话记录详情页
        print('test_getin_call_record_detail')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
        time.sleep(3)
        lv_contact_log = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'lv_contact_log')
        calllog_set = lv_contact_log.find_elements_by_android_uiautomator('className("android.widget.RelativeLayout")')
        #点击第一条通话记录
        calllog_set[1].find_element_by_id(self.commonCls.debug_id_pre+'call_log_info').click()
    #     com.yealink.uc.android.alpha:id/title
        time.sleep(3)
        ele = self.driver.find_element_by_android_uiautomator("text(\"通话详情\")")
        self.commonCls.result_handler(self.driver,'exsit',ele,'未进入通话记录详情界面')
    def test_4detail_title(self):#检查通话记录详情标题
        print('test_detail_title')
        # com.yealink.uc.android.alpha:id/title
        detail_title_ele = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'title')
        detail_title = detail_title_ele.get_attribute('text')
        print('detail_title')
        print(detail_title)
        result = detail_title == '通话详情'
        self.commonCls.result_handler(self.driver,'equal',result,'通话详情页标题未显示')
        # self.commonCls.result_handler(self.driver,result,'通话详情页标题未显示！')
    def test_5detail_call_type(self):#检查通话记录详情最后一路通话的通话类型
        print('test_detail_call_type')
        detail_calltype_ele = self.driver.find_elements_by_id(self.commonCls.debug_id_pre+'tv_call_protocol')
        detail_call_type = detail_calltype_ele[0].get_attribute('text')
        print('detail_call_type')
        print(detail_call_type)
        result = detail_call_type == self.call_type
        # self.commonCls.result_handler(self.driver,result,'通话详情页的通话类型与实际通话类型不符！')
        self.commonCls.result_handler(self.driver,'equal',result,'通话详情页的通话类型与实际通话类型不符')
    def test_6detail_call_num(self):#检查通话记录详情的号码
        print('test_detail_call_num')
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        # 滑动屏幕--上滑
        # self.driver.swipe(width*0.5, height*0.75, width*0.5, height*0.25, 180000)
        self.commonCls.swipeUp(self.driver,1000)
        time.sleep(5)

        # 点击分机号
        self.driver.find_element_by_android_uiautomator("text(\"通话详情\")").click()
        #获取分机号值
        detail_callnum_ele = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'item_contact_detail_subtitle')
        detail_call_num = detail_callnum_ele.get_attribute('text')
        print(detail_call_num)
        result = detail_call_num == self.call_num_str
        # self.commonCls.result_handler(self.driver,result,'通话详情页的通话号码与实际通话号码不符！')
        self.commonCls.result_handler(self.driver,'equal',result,'通话详情页的通话类型与实际通话类型不符')
        self.driver.quit()
# if __name__== '__main__':
#     unittest.main(verbosity=2)
