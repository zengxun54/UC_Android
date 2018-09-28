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


class Testsetadmin(unittest.TestCase):
    """
    uc登录的case
    """
    # desired_caps = connectmobile()
    # print(desired_caps)


    def setUp(self):
        print("Test start setadmin......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testsetadmin(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"创建群\")").click()
        time.sleep(5)
        #增加断言判断检查页面是否有展示出来
        head=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/group_icon')
        try:
            self.assertIsNotNone(head)
            print('创建群页面展示成功')
            #saveScreenshot.saveScreenshot(self.driver, "创建群页面展示成功")
        except AssertionError as e:
            raise('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        name1 = random.randint(0,100)
        name2 = 'liujxsetadmin'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
        time.sleep(2)
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('liaozz')
        # self.driver.hide_keyboard()
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
        #设置管理员操作
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/rllt_accredit_manager').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator("text(\"廖珍珍\")").click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        time.sleep(4)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()
        #判断管理员是否设置成功
        list_mem_level = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').text
        try:
            self.assertEqual(list_mem_level,'管理员')
            print('管理员设置成功功能正常')
        except AssertionError as e:
            print('管理员设置失败')
            saveScreenshot.saveScreenshot(self.driver, "管理员设置失败")
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()
        pass