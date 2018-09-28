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


class Testcasetalkfile(unittest.TestCase):
    """
    uc登录的case
    """
    # desired_caps = connectmobile()
    # print(desired_caps)


    def setUp(self):
        print("Test start talkfile......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testcasetalkfile(self):
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
        name2 = 'liujxtalkfile'+ str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_search').send_keys('liaozz')
        #self.driver.hide_keyboard()
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
        #在聊天窗口中发送文件
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/radio_more').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"文件\")").click()
        #print('加号选项正常打开')
        time.sleep(4)
        get_title=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_group_name').text
        #print(get_title)
        #判断第一个是不是txt，不是的话滑动页面，找到txt进行点击,若是则点击第一个文件
        ###需要补充txt下如果没有文件就报错的情况
        ####
        ####
        ####
        if get_title !='TXT':
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            i = 0
            while i < 20:
                try:
                    self.driver.find_element_by_android_uiautomator("text(\"TXT\")").click()
                    break
                except Exception as e:
                    self.driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
                    i = i + 1
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/file_content').click()
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/menu_send').click()
        else:
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/file_content').click()
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/menu_send').click()
        time.sleep(5)
        #获取到聊天窗口中的文件名称
        file_name =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_name').text
        #print(file_name)
        #上述是发送文件，以下是对比文件是否发送成功比对文件名、文件大小、文件状态
        #先等待多少秒后看是否能获取到进度名称，可能得加上时间判断，一定时间后若获取到就接着获取状态，若获取不到就报错下
        #获取文件大小100M作区分，100M以上30秒，100M以下20秒(后面再完善)###
        #再发送成功的基础上，去查看统计条数是否有增加另外获取到的和发送的是否是同一封
        #talk_filename=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_name').text
        #file_size =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_size').text
        #print(123)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_status'))
        status1=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_status').text
        try:
            self.assertEqual(status1,"已发送")
            print('文件发送成功')
        except AssertionError as e:
            print('文件发送失败')
            saveScreenshot.saveScreenshot(self.driver, "文件发送失败")
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"文件\")").click()
        time.sleep(2)
        list_name = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/file_name').text
        try:
            self.assertEqual(list_name, file_name)
            print('聊天文件成功功能正常')
        except AssertionError as e:
            print('聊天文件失败')
            saveScreenshot.saveScreenshot(self.driver, "聊天文件失败")
        #is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())
        #talk_status =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_file_status').text

    def tearDown(self):
        self.driver.quit()
        pass