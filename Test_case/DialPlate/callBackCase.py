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
        # self.driver.quit()
        #@通话记录回拨
    def test_1calllog_back(self):
        print('test_1calllog_back')
        xpathStr_bohao = "//android.widget.TextView[@text='拨号']"
        self.commonCls.waitForElementByType(self.driver,'xpath', xpathStr_bohao)#等待
        self.driver.find_element_by_xpath(xpathStr_bohao).click()
        # self.driver.find_element_by_android_uiautomator("text(\"拨号\")").click()
        print('xpathStr_bohao')
        time.sleep(2)
        lv_contact_log = self.driver.find_element_by_id(self.commonCls.debug_id_pre+'lv_contact_log')
        #获取第1个通话记录的通话类型
        self.first_calllog_type = self.commonCls.get_first_calllog_info(self.driver,'call_log_protocol')
        print(self.first_calllog_type)
        #获取通话记录集合
        # xpathStr = "//android.widget.TextView[@text='拨号']"
        calllog_set = lv_contact_log.find_elements_by_class_name("android.widget.RelativeLayout")
        calllog_set[1].click()
        print(len(calllog_set))
        idStr=(commonClass.debug_id_pre+'nameContainer')
        time.sleep(5)
        ele = self.driver.find_element_by_android_uiautomator('resourceId("'+idStr+'")')
        ##############################################
        self.commonCls.result_handler(self.driver,'exsit',ele,'通话记录回拨失败')
        # self.commonCls.result_handler(self.driver,result,'通话记录回拨失败！')
    #############################################
    def test_2check_call_type(self):
        idStr_nameContainer = commonClass.debug_id_pre+'nameContainer'#等待
        self.commonCls.waitForElementByType(self.driver,'id', idStr_nameContainer)
        print('test_2check_call_type')
        debug_id_pre = commonClass.debug_id_pre
        self.driver.find_element_by_id(idStr_nameContainer).click()#判断通话界面图标是否出现
        source = self.driver.page_source
        print(self.first_calllog_type)
        el_button = debug_id_pre+'stopVideo'
        button = '摄像头按钮'
        if self.first_calllog_type == '[音频通话]':
            el_button = debug_id_pre+'switchSpeaker'
            button = '扬声器按钮'
        idStr_nameContainer = commonClass.debug_id_pre+'nameContainer'
        self.commonCls.waitForElementByType(self.driver,'id', idStr_nameContainer)#等待
        self.driver.find_element_by_id(idStr_nameContainer).click()#通话界面图标
        msg = self.first_calllog_type+'界面没有'+button
        ele = self.driver.find_element_by_android_uiautomator('resourceId("'+el_button+'")')
        time.sleep(1)
        self.commonCls.result_handler(self.driver,'exsit',ele,msg)
         # #挂断通话
        print('test_2check_call_type')
        self.commonCls.hang_up(self.driver)
        time.sleep(5)
        ele = self.driver.find_element_by_android_uiautomator("text(\"拨号\")")
        self.commonCls.result_handler(self.driver,'exsit',ele,'通话界面未关闭')
        self.driver.quit()
# if __name__== '__main__':
#     unittest.main(verbosity=2)
