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

class TestGsetAnnouncement(unittest.TestCase):
    def setUp(self):
        print("Test start setannou......")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #d.app_start(desired_caps)
        time.sleep(5)
        return

    def testGsetAnnouncement(self):
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
            raise ('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        name1 = random.randint(0,100)
        name2 = 'liujxannou'+ str(name1)

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
        try:
            self.assertEqual(con_name,name2)
            print('创建群成功')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
        #设置群公告操作
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        # # 增加断言判断检查设置页面是否有展示出来
        shead = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_group_number').text
       # print(shead)
       #  try:
       #      self.assertEqual(shead,'10050743')
       #      #saveScreenshot.saveScreenshot(self.driver, "群设置页面展示成功")
       #  except AssertionError as e:
       #      saveScreenshot.saveScreenshot(self.driver, "群设置页面展示失败")
       #      AssertionError:('群设置页面展示失败')
        time.sleep(3)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/group_chat_setting_bulletin').click()
        #print('进入群公告页面成功')
        time.sleep(3)

        "判断是否已有群公告"
        try:
            annou = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_empty')
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_publish').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').send_keys('zzzz')
            self.driver.find_element_by_android_uiautomator("text(\"发布\")").click()
            editannou=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_title').text
            try:
                self.assertEqual(editannou, 'zzzz')
                saveScreenshot.saveScreenshot(self.driver, "群公告新增成功功能正常")
            except AssertionError as e:
                saveScreenshot.saveScreenshot(self.driver, "群公告新增失败")
                raise('群公告新增失败')
        except:
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_edit').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').send_keys('abcd')
            self.driver.find_element_by_android_uiautomator("text(\"发布\")").click()
            newannou = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_title').text
            try:
                self.assertEqual(newannou, 'abcd')
                saveScreenshot.saveScreenshot(self.driver, "群公告修改成功功能正常")
            except AssertionError as e:
                saveScreenshot.saveScreenshot(self.driver, "群公告修改失败")
                raise('群公告修改失败')
        # annou=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_empty')
        # #print(annou)
        # if annou is False:
        #     self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_edit').click()
        #     time.sleep(2)
        #     self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').send_keys('abcd')
        #     self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        #     newannou = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_title').text
        #     try:
        #         self.assertEqual(newannou, 'abcd')
        #         saveScreenshot.saveScreenshot(self.driver, "群公告修改成功")
        #     except AssertionError as e:
        #         saveScreenshot.saveScreenshot(self.driver, "群公告修改失败")
        #         AssertionError: ('群公告修改失败')
        # else:
        #     self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_publish').click()
        #     time.sleep(2)
        #     self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').send_keys('zzzz')
        #     self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        #     editannou=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_title').text
        #     try:
        #         self.assertEqual(editannou, 'abcd')
        #         saveScreenshot.saveScreenshot(self.driver, "群公告新增成功")
        #     except AssertionError as e:
        #         saveScreenshot.saveScreenshot(self.driver, "群公告新增失败")
        #         AssertionError: ('群公告新增失败')

        #stitle = self.driver.find_elements_by_android_uiautomator("text(\"编辑名称\")")
        # try:
        #     self.assertIsNotNone(stitle)
        #     #saveScreenshot.saveScreenshot(self.driver, "编辑名称页面展示成功")
        # except AssertionError as e:
        #     saveScreenshot.saveScreenshot(self.driver, "编辑名称页面展示失败")
        #     AssertionError:('编辑名称页面展示失败')
        #oldname = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit').text
        # newname = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/personal_detail_edit')
        # newname.send_keys('newliujx1')
        # self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_confirm').click()
        # time.sleep(2)
        # #校验下是否修改成功
        # con_name =self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/tv_group_name').text
        # try:
        #     self.assertEqual(con_name,'newliujx1')
        #     saveScreenshot.saveScreenshot(self.driver, "群名称修改成功")
        # except AssertionError as e:
        #     saveScreenshot.saveScreenshot(self.driver, "群名称修改失败")
        #     AssertionError:('群名称修改失败')

    def tearDown(self):
        self.driver.quit()
        pass
