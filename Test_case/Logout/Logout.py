# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time
import  configparser
import HTMLTestRunner
from Public import commonClass


class Login (unittest.TestCase):
    def setUp(self):
        print('Logout setup')
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
    def tearDown(self):
        pass
    def test_logout(self):
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
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
        el = (commonClass.debug_id_pre+'btn_login')
        try:
            assert el in source
        except Exception as msg:
            print('失败！')
            raise('Fail') #抛出异常这个用例就不会pass了

# if __name__== '__main__':
#     unittest.main ()