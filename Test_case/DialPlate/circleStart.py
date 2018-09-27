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

    def test_4wait(self):
        time.sleep(60)
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
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