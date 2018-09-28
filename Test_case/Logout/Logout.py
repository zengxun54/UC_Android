# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
import  configparser
import HTMLTestRunner


class Login (unittest.TestCase):
    def setUp(self):
        desired_cups = {}
        # 设备平台
        desired_cups['platformName'] = 'Android'
        # 设备系统版本
        desired_cups['platformVersion'] = '8.0.0'
        # 设备名称
        desired_cups['deviceName'] = 'SJE0217421000430'
        # apk安装包路径
        PATH = lambda p: os.path.abspath (os.path.join (os.path.dirname (__file__), p))
        desired_cups['app'] = PATH (r'C:\Users\yl1477\Desktop\Yealink_UC_Android_1.0.295.1010-local-release.apk')
        # 启动app
        self.driver = webdriver.Remote ('http://localhost:4723/wd/hub', desired_cups)
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        time.sleep (10)

    def tearDown(self):
        self.driver.find_element_by_id('com.yealink.uc.android:id/btn_login').click()


    def test_logout(self):
        conf = configparser.ConfigParser ()
        conf.read ("../../config/parameters.ini", encoding='utf-8')
        # 点击左上角个人头像
        self.driver.find_element_by_id (conf.get('个人中心','个人头像')).click ()
        time.sleep (3)
        # 点击设置
        self.driver.find_element_by_id (conf.get('个人中心','设置')).click ()
        time.sleep (3)
        # 点击退出当前账号
        self.driver.find_element_by_id (conf.get('个人中心','退出当前账号')).click ()
        time.sleep (5)
        # 点击确定
        self.driver.find_element_by_id (conf.get('个人中心','确定退出')).click ()
        source = self.driver.page_source
        el = ('com.yealink.uc.android:id/btn_login')
        try:
            assert el in source
        except Exception as msg:
            print ('失败！')
            raise 'Fail' #抛出异常这个用例就不会pass了

if __name__== '__main__':
    unittest.main ()