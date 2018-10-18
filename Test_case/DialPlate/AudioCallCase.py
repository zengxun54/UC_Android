# # -*- encoding:utf-8 -*-
# import unittest
# from appium import webdriver
# import os
# import time
# from Public import commonClass
# # from test_mathfunc import TestMathFunc
# import HTMLTestRunner
# import traceback
#
# class AudioCallCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         debug_id_pre = 'com.yealink.uc.android.alpha:id/'
#         self.commonCls = commonClass.commonCase(debug_id_pre)
#         print('setup')
#         desired_cups = {}
#         # 设备平台
#         desired_cups['platformName'] = 'Android'
#         # 设备系统版本
#         desired_cups['platformVersion'] = '8.0.0'
#         # 设备名称
#         desired_cups['deviceName'] = 'SJE0217421000430'
#         # apk安装包路径
#         PATH = lambda p: os.path.abspath(os.path.join (os.path.dirname (__file__), p))
#         desired_cups['app'] = PATH (r'F://Android//apk//Yealink_UC_Android_1.0.294.1001-pre-debug.apk')
#         # 启动app
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cups)
#         # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
#         time.sleep(5)
#     @classmethod
#     def tearDownClass(self):
#         print('tearDown')
#         # pass
#     # @unittest.skip("demonstrating skipping")
#     def test_1call_num(self):#拨号用例
#         print('13')
#         debug_id_pre = 'com.yealink.uc.android.alpha:id/'
#         call_num_str = '2784'
#         # dialer_bar = debug_id_pre+'dialer_bar'
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//android.widget.TextView[@text='拨号']").click()
#         time.sleep(3)
#         # driver = self.driver
#         self.commonCls.test_click_num(self.driver,call_num_str)
#         time.sleep(1)
#         # 点击拨号
#         self.driver.find_element_by_id(debug_id_pre+'iv_call_send').click()
#         time.sleep(3)
#         self.driver.find_element_by_id(debug_id_pre+'name').click()#判断通话界面图标是否出现
#         time.sleep(2)
#         source = self.driver.page_source
#         el=('com.yealink.uc.android.alpha:id/iconEncrypt')
#         try:
#             assert el in source
#         except Exception as msg:
#             # print('未进入通话界面！')
#             raise ('未进入通话界面')
#     def test_2hang_up(self):#挂断通话
#         print('hang up')
#         debug_id_pre = 'com.yealink.uc.android.alpha:id/'
#         # com.yealink.uc.android.alpha:id/left_btn
#         time.sleep(3)
#         self.driver.find_element_by_id(debug_id_pre+'name').click()#判断通话界面图标是否出现
#         time.sleep(1)
#         clickRes = self.driver.find_element_by_id(debug_id_pre+'hangup').click()#挂断通话
#         time.sleep(3)
#         iv_call_send = (debug_id_pre+'tv_recent_calllog_title')
#         source = self.driver.page_source
#         try:
#             assert iv_call_send in source
#         except Exception as msg:
#             # print('未进入通话界面！')
#             raise ('通话界面未挂断')
#     def test_3wait(self):
#         time.sleep(60)
# if __name__== '__main__':
#       unittest.main(verbosity=2)
# #     suite = unittest.TestSuite()
# #     # 将测试用例加入到测试容器中
# #     print(suite)
# #     suite.addTests([AudioCallCase('test_1call_num'),AudioCallCase('test_2hang_up')])
# #     report_path = r'E:\testresult.html'
# #     fp = open(report_path, "wb")
# #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
# #     runner.run(suite)
# #     print('123')
# #     fp.close()

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

class AudioCallCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    @classmethod
    def setUpClass(self):
        print('AudioCallCase setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        self.first_calllog_type  = '[视频通话]'
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @unittest.skip("demonstrating skipping")
    @classmethod
    def tearDownClass(self):
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.commonCls.restart_adb()
        print('tearDown')
        # self.driver.quit()
        #@通话记录回拨
    @unittest.skip("demonstrating skipping")
    def test_1call_num(self):#拨号用例
        print('audiocall case')
    @unittest.skip("demonstrating skipping")
    def test_4wait(self):
        time.sleep(60)
# if __name__== '__main__':
#     unittest.main(verbosity=2)
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