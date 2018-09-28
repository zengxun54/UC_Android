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
import random
from common.ConnectMobile import connectmobile
from common import saveScreenshot
import uiautomator2 as u2

class TestGsetName(unittest.TestCase):
    def setUp(self):
        print("Test start setname......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #d.app_start(desired_caps)
        time.sleep(5)
        return

    def testgsetName(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"创建群\")").click()
        time.sleep(5)
        # 增加断言判断检查页面是否有展示出来
        head = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/group_icon')
        try:
            self.assertIsNotNone(head)
            print('创建群页面展示成功')
            #saveScreenshot.saveScreenshot(self.driver, "创建群页面展示成功")
        except AssertionError as e:
            AssertionError: ('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        name1 = random.randint(0, 100)
        name2 = 'liujxsetname' + str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
        time.sleep(2)
        # self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('liaozz')
        self.driver.hide_keyboard()
        time.sleep(4)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_icon').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"创建\")").click()
        time.sleep(2)
        # 判断是否进入聊天窗口来确认页面创建成功
        con_name = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text
        #print(con_name)
        try:
            self.assertEqual(con_name, name2)
            print('创建群成功')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_group_name').click()
        stitle = self.driver.find_elements_by_android_uiautomator("text(\"编辑名称\")")
        try:
            self.assertIsNotNone(stitle)
        except AssertionError as e:
            saveScreenshot.saveScreenshot(self.driver, "编辑名称页面展示失败")
            AssertionError:('编辑名称页面展示失败')
        #oldname = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').text
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').send_keys('newliujx1')
        self.driver.hide_keyboard()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_confirm').click()
        time.sleep(2)
        #校验下是否修改成功
        con_name =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_group_name').text
        try:
            self.assertEqual(con_name,'newliujx1')
            print('群名称修改正常功能正常')
        except AssertionError as e:
            saveScreenshot.saveScreenshot(self.driver, "群名称修改失败")
            AssertionError:('群名称修改失败')

    def tearDown(self):
        self.driver.quit()
        pass
