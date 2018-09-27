# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
from Public import commonClass
# from test_mathfunc import TestMathFunc
import HTMLTestRunner
import traceback

class VideoCallCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDownClass(self):
        print('tearDown')
        # pass
    # @unittest.skip("demonstrating skipping")
    def test_1call_num(self):#拨号用例
        # print('13')
        # debug_id_pre = commonClass.debug_id_pre
        call_num_str = '4001'
        result = self.commonCls.call_num(self.driver,call_num_str)
        self.commonCls.result_handler(result,"未进入通话界面")
    def test_2call_statstic(self):
        print('23')
        debug_id_pre = commonClass.debug_id_pre
        # com.yealink.uc.android.alpha:id/time_container
        # self.driver.find_element_by_id(debug_id_pre+self.paramter.get("dialPlate", "time_container")).click()
        self.driver.find_element_by_id(self.commonCls.get_conf("dialPlate","time_container")).click()
        # self.driver.find_element_by_id(debug_id_pre+'time_container').click()
        time.sleep(1)
        # 判断发送分辨率或帧率是否为0
        black_screen_send = self.commonCls.get_resolution_and_fps(self.driver)
        try:
            assert black_screen_send
        except Exception as msg:
            raise ('发送分辨率或帧率为0')
        self.driver.find_element_by_name('接收').click()
        black_screen_resv = self.commonCls.get_resolution_and_fps(self.driver)
        try:
            assert black_screen_resv
        except Exception as msg:
            raise ('接收分辨率或帧率为0')
    def test_3hang_up(self):#挂断通话
        debug_id_pre = commonClass.debug_id_pre
        time.sleep(1)
        # self.driver.find_element_by_id(debug_id_pre+self.paramter.get("dialPlate", "left_btn")).click()
        self.driver.find_element_by_id(self.commonCls.get_conf("dialPlate","left_btn")).click()
        # self.driver.find_element_by_id(self.commonCls.debug_id_pre+'left_btn').click()
        time.sleep(1)
        self.commonCls.hang_up(self.driver)
        time.sleep(10)
        # iv_call_send = (debug_id_pre+self.paramter.get("dialPlate", "calllog_title"))
        iv_call_send = (self.commonCls.get_conf("dialPlate","calllog_title"))
        source = self.driver.page_source
        try:
            assert iv_call_send in source
        except Exception as msg:
            # print('未进入通话界面！')
            raise ('通话界面未挂断')
    def test_4wait(self):
        time.sleep(60)
if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite = unittest.TestSuite()
    # # 将测试用例加入到测试容器中
    # print(suite)
    # suite.addTests([VideoCallCase('test_1call_num'),VideoCallCase('test_2call_statstic'),VideoCallCase('test_3hang_up')])
    # report_path = r'E:\testresult.html'
    # fp = open(report_path, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
    # runner.run(suite)
    # print('123')
    # fp.close()