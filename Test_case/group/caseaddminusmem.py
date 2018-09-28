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
from selenium.webdriver.support.ui import WebDriverWait
from collections import *

class Testaddminusmem(unittest.TestCase):


    def setUp(self):
        print("Test start addminusmem...")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testaddminusmem(self):
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
            AssertionError:('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        name1 = random.randint(0,100)
        name2 = 'liujxaddmem'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('liaozz')
        time.sleep(4)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_icon').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"创建\")").click()
        time.sleep(2)
        #判断是否进入聊天窗口来确认页面创建成功
        con_name=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text
        #print(con_name)
        try:
            self.assertEqual(con_name,name2)
            print('创建群成功')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        list1= self.driver.find_elements_by_id('com.yealink.uc.android.alpha:id/member_icon')
        #print(list1)
        res = len(list1)-2
        #print(res)
        list1[2].click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('luzf')
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_icon').click()
        self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        time.sleep(3)
        list_add = self.driver.find_elements_by_id('com.yealink.uc.android.alpha:id/member_icon')
        res_add=len(list_add)-2
        #print(res_add)
        try:
            self.assertEqual(res_add-1, res)
            print('增加成员成功，功能正常')
        except AssertionError as e:
            print('增加成员失败')
            saveScreenshot.saveScreenshot(self.driver, "增加成员失败")
        #删除成员
        list2 = self.driver.find_elements_by_id('com.yealink.uc.android.alpha:id/member_icon')
        list2[4].click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"廖珍珍\")").click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        #判断成员人数来验证
        list_minus = self.driver.find_elements_by_id('com.yealink.uc.android.alpha:id/member_icon')
        res_minus=len(list_minus)-2
        try:
            self.assertEqual(res_minus+1,res_add)
            print('删除成员成功，功能正常')
        except AssertionError as e:
            print('删除成员失败')
            saveScreenshot.saveScreenshot(self.driver, "删除成员失败")
    def tearDown(self):
        self.driver.quit()
        pass