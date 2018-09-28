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

class Testtalk(unittest.TestCase):
    """
    uc登录的case
    """
    # desired_caps = connectmobile()
    # print(desired_caps)


    def setUp(self):
        print("Test start talk......")
        desired_caps = connectmobile()
       #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testtalk(self):
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
        name2 = 'liujxtalk'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
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
        self.driver.find_element_by_id("com.yealink.uc.android.alpha:id/chat_bar_editor").send_keys('@')
        #self.driver.hide_keyboard()
        #print('输入@')
        time.sleep(3)
        # 增加断言判断检查设置页面是否有展示出来
        shead = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_all_member').text
        #print(shead)
        try:
            self.assertEqual(shead,'全体成员')
            print('@页面展示成功')
        except AssertionError as e:
            print('@页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "@页面展示失败")
        self.driver.find_element_by_android_uiautomator("text(\"廖珍珍\")").click()
        edit1=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').text
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator("text(\"发送\")").click()
        time.sleep(3)
        list_records=self.driver.find_elements_by_id('com.yealink.uc.android.alpha:id/record_content')
        record=list_records[2].text
        try:
            self.assertEqual(edit1,record)
            print('@发送功能成功功能正常')
        except AssertionError as e:
            print('@发送功能失败')
            saveScreenshot.saveScreenshot(self.driver, "@发送功能失败")
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        pass
