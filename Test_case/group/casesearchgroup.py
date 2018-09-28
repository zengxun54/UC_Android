#!/usr/bin/env python
#coding = utf-8
__author__ = 'liujx'

import os
import sys
import importlib

importlib.reload(sys)
sys.path.append("common")
import unittest
from appium import webdriver
from time import sleep
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
import configparser
import time
from common.ConnectMobile import connectmobile
from common import saveScreenshot
import uiautomator2 as u2

class Testsearchgroup(unittest.TestCase):
    def setUp(self):
        print("Test start searchgroup......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return

    def testsearchgroup(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        #saveScreenshot.saveScreenshot(self.driver, "元素没加载出来")
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator("text(\"查找群\")").click()
        time.sleep(3)
        all_group =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_title').text
        try:
            self.assertEqual(all_group, '全部群')
            #saveScreenshot.saveScreenshot(self.driver, "群搜索页面展示成功")
        except AssertionError as e:
            saveScreenshot.saveScreenshot(self.driver, "群搜索页面展示失败")
            raise('群搜索页面展示失败')
        search = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit')
        page="liujx"
        search.send_keys(page)
        self.driver.hide_keyboard()
        time.sleep(3)
        #尝试获取搜索结果第一行的群名称
        list1=self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
        try:
            self.assertIsNotNone(list1) and self.assertIn(list1 in  page)
            print('查找群成功功能正常')
        except AssertionError as e:
            raise('查找群失败')
            saveScreenshot.saveScreenshot(self.driver, "查找群失败")
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        pass
