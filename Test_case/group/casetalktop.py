#!/usr/bin/env python
# coding = utf-8

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


class Testtalktop(unittest.TestCase):

    def setUp(self):
        print("Test start talktop......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testtalktop(self):
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
        name2 = 'liujxtop'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
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
        #判断是否进入聊天窗口来确认页面创建成功
        con_name=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text
        try:
            self.assertEqual(con_name,name2)
            print('创建群成功')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
        #设置会话置顶操作
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/switch_top').click()
        time.sleep(2)
        #返回到聊天页面
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()
        time.sleep(2)
        #返回到最近消息列表
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()
        #验证会话置顶功能
        #创建新会话
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_search').click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit').send_keys('liaozz')
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_name').click()
        self.driver.find_element_by_android_uiautomator("text(\"发消息\")").click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').send_keys('abc')
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"发送\")").click()
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()
        #对比会话位置
        top_name = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/name').text
        #print(top_name)
        try:
            self.assertEqual(top_name,name2)
            print('会话置顶成功功能正常')
        except AssertionError as e:
            print('会话置顶失败')
            saveScreenshot.saveScreenshot(self.driver, "会话置顶失败")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        pass