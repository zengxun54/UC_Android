#Author:Joy Tang
#-*- coding: utf-8 -*-

import os, sys, time
from appium import webdriver
import unittest
import random

#debug包
packageName = 'com.yealink.uc.android.alpha:id/'

class publicMethod(unittest.TestCase):

    #打开APP
    def open_app(self):
        desired_cups = {}
        desired_cups['platformName'] = 'Android'
        desired_cups['platformVersion'] = '8.0.0'
        desired_cups['deviceName'] = '6423b456'
        #desired_cups['app'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\app\\' + 'Yealink_UC_Android_1.1.3.839-pre-debug.apk'
        desired_cups['app'] = 'F:\Yealink_UC_Android_1.1.16.1024-pre-debug.apk'
        desired_cups['appPackage'] = 'com.yealink.uc.android.alpha'
        desired_cups['appActivity'] = 'com.yealink.uc.android.StartActivity'
        desired_cups['unicodeKeyboard'] = True
        desired_cups['resetKeyboard'] = True
        desired_cups['noReset'] = True
        desired_cups['automationName'] = 'uiautomator2'


        #判断是否连上，连不上则重新连10次
        for i in range(1, 10):
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cups)
            # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
            time.sleep(10)
            title = self.driver.find_element_by_id(packageName + 'title').text
            try:
                self.assertEqual(title, "消息")
                return self.driver
            except AssertionError as e:
                if i == 10:
                    AssertionError("连接失败")
                    raise
                i += 1


    #获取当前登录的用户名
    def get_username(self):
        try:
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/iv_head').click()
            time.sleep(1)
            username = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/user_name').text
            self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_btn').click()
            time.sleep(1)
            return username
        except:
            self.driver = publicMethod.open_app(self)


    #打开一个讨论组IM界面
    def open_discussionIm(self):
        #进入联系人-讨论组列表选择一个讨论组
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.yealink.uc.android.alpha:id/tabStrip']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/contact_my_groups').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id='com.yealink.uc.android.alpha:id/expandable_list']/android.widget.RelativeLayout[1]").click()
        time.sleep(2)

        #正常打开讨论组IM界面
        try:
            self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor'))
            print("打开讨论组IM成功")
            return self.driver
        except AssertionError as e:
            AssertionError("打开讨论组IM失败")
            raise

    #随机刷屏函数
    # def shuaping(self):
    #     for i in range(1, 10):
    #         number = random.randint(0, 1000)
    #         self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
    #         time.sleep(1)
    #         self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').send_keys("刷屏!%s" % number)
    #         time.sleep(1)
    #         #self.driver.find_element_by_android_uiautomator('new UiSelector().text(\"发送\"').click()
    #         self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send').click()
    #         time.sleep(1)
    #         i += 1

    #打开讨论组设置界面---跳转后取不到元素，先注释
    def open_discussionSetting(self):
        self.driver = publicMethod.open_discussionIm(self)
        #进入设置界面
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting').click()
        time.sleep(2)
        try:
            self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/discussion_chat_setting_icon'))
            print("打开讨论组设置界面成功")
        except AssertionError as e:
            AssertionError("打开讨论组设置界面失败")








