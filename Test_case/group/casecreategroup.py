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


class Testcreategroup(unittest.TestCase):
    """
    uc登录的case
    """
    # desired_caps = connectmobile()
    # print(desired_caps)


    def setUp(self):
        print("Test start creategroup....")
        desired_caps = connectmobile()
        #print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        return driver

    def testcreategroup(self):
        time.sleep(5)
        #点击加号展示出入口
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        #saveScreenshot.saveScreenshot(self.driver, "元素没加载出来")
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"创建群\")").click()
        time.sleep(2)
        # 检查页面是否有展示出来
        head=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/group_icon')
        try:
            self.assertIsNotNone(head)
            print('创建群页面展示成功')
            #saveScreenshot.saveScreenshot(self.driver, "创建群页面展示成功")
        except AssertionError as e:
            raise('创建群页面展示失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群页面展示失败")
        #获取群名称灰色提示语
        groupname=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').text
        #获取群名称提示长度
        name_length=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name_length_tip').text
        #获取群公告灰色提示语
        annoumessage=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_bulletin').text
        #获取群公告提示长度
        annou_length=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_bulletin_length_tip').text
        #获取按钮名称
        create_button=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').text
        #校验获取值是否与预期一致
        #校验群名称灰色提示语
        try:
            self.assertEqual(groupname,'请填写群名称(必填，20字)')
            print('群名称灰色提示语内容正确')
        except AssertionError as e:
            print('群名称灰色提示语内容错误')
            saveScreenshot.saveScreenshot(self.driver, "群名称灰色提示语内容错误")
        #校验群名称长度
        try:
            self.assertEqual(name_length,'20')
            print('群名称长度正确')
        except AssertionError as e:
            print('群名称长度错误')
            saveScreenshot.saveScreenshot(self.driver, "群名称长度错误")
        #校验群公告灰色提示语
        try:
            self.assertEqual(annoumessage,'添加群公告(选填，100字)')
            print('群公告灰色提示语内容正确')
        except AssertionError as e:
            print('群公告灰色提示语内容错误')
            saveScreenshot.saveScreenshot(self.driver, "群公告灰色提示语内容错误")
        #校验群公告长度
        try:
            self.assertEqual(annou_length,'100')
            print('群公告长度文字正确')
        except AssertionError as e:
            print('群公告长度文字错误')
            saveScreenshot.saveScreenshot(self.driver, "群公告长度文字错误")
        #校验按钮名称
        try:
            self.assertEqual(create_button,'下一步：选择联系人')
            print('按钮名称文字正常')
        except AssertionError as e:
            print('按钮名称文字错误')
            saveScreenshot.saveScreenshot(self.driver, "按钮名称文字错误")
        name1 = random.randint(0, 100)
        name2 = 'liujxcreat' + str(name1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/edit_group_name').send_keys(name2)
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_next').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("text(\"创建\")").click()
        time.sleep(2)
        #判断是否进入聊天窗口来确认页面创建成功
        con_name=self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text
        #print(con_name)
        try:
            self.assertEqual(con_name,name2)
            print('创建群成功功能正常')
        except AssertionError as e:
            print('创建群失败')
            saveScreenshot.saveScreenshot(self.driver, "创建群失败")
    def tearDown(self):
        self.driver.quit()
        pass
# if __name__== '__main__':
#     unittest.main(verbosity=2)