#!/usr/bin/env python
# coding = utf-8
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
import random
from common.ConnectMobile import connectmobile
from common import saveScreenshot


class Testdisgroup(unittest.TestCase):
    """
    uc登录的case
    """
    # desired_caps = connectmobile()
    # print(desired_caps)


    def setUp(self):
        print("Test start disgroup......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testdisgroup(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"创建群\")").click()
        time.sleep(2)
        #增加断言判断检查页面是否有展示出来
        head=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/group_icon')
        try:
            self.assertIsNotNone(head)
            print('创建群页面展示成功')
        except AssertionError as e:
            raise('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        name1 = random.randint(0,100)
        name2 = 'liujxdis'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        #self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('liaozz')
        #time.sleep(4)
        #self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_icon').click()
        #time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"创建\")").click()
        time.sleep(2)
        #判断是否进入聊天窗口来确认页面创建成功
        con_name=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text
        print(con_name)
        try:
            self.assertEqual(con_name,name2)
            print('创建群成功')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
        #设置解散群操作
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        time.sleep(2)
        #滑动屏幕查找到解散该群
        width = self.driver.get_window_size()['width']
        height =self.driver.get_window_size()['height']
        self.driver.get_window_size()
        i=0
        while i < 10:
            try:
                self.driver.find_element_by_android_uiautomator("text(\"解散该群\")").click()
                break
            except Exception as e:
                self.driver.swipe(width/2,height*0.8,width/2,height*0.2)
                i=i+1
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        #验证解散群功能
        time.sleep(2)
        dis_group = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/name').text
        print(dis_group)
        try:
            self.assertNotEqual(dis_group,name2)
            print('群解散成功功能正常')
        except AssertionError as e:
            print('群解散失败')
            saveScreenshot.saveScreenshot(self.driver, "群解散失败")

    def tearDown(self):
        self.driver.quit()
        pass