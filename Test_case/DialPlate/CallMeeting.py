# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
import random
class CallMeeting(unittest.TestCase):
    def setUp(self):
            desired_cups = {}
            # 设备平台
            desired_cups['platformName'] = 'Android'
            # 设备系统版本
            desired_cups['platformVersion'] = '5.0.1'
            # 设备名称
            desired_cups['deviceName'] = '69DDU16513003941'
            # apk安装包路径
            PATH = lambda p: os.path.abspath (os.path.join (os.path.dirname (__file__), p))
            desired_cups['app'] = PATH ('C:\Users\yl1477\Desktop\Yealink_UC_Android_1.0.291.982-pre-debug.apk')
            # 启动app
            self.driver = webdriver.Remote ('http://localhost:4723/wd/hub', desired_cups)
            # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
            time.sleep (5)
    def tearDown(self):
        self.driver.find_element_by_id ('com.yealink.uc.android.alpha:id/iconEncrypt,').click ()  # 点击盾牌图标
        time.sleep(2)
        self.driver.find_element_by_id ('com.yealink.uc.android.alpha:id/hangup').click ()  # 挂断通话
        time.sleep (2)
        self.driver.find_element_by_id ('com.yealink.uc.android.alpha:id/btnCancel').click ()  # 结束会议
    def test_callmeeting(self):
        abc=random.randint(2523,2536)
        self.driver.find_element_by_name('拨号').click()#切换到拨号盘界面
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/et_dialpad_tel').send_keys(abc)#输入会议号码
        self.driver.hide_keyboard()#收起手机键盘
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/iv_call_send').click() #点击拨号图标呼出
        time.sleep (20)
        source = self.driver.page_source
        el = ('com.yealink.uc.android.alpha:id/textView')
        try:
            assert el in source
        except Exception as msg:
            print '失败！'
            raise 'Fail'

if __name__== '__main__':
    unittest.main ()