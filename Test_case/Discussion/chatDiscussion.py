#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
import time
import unittest
import random
import uiautomator2 as u2

sys.path.append("..")
from Public.publicMethod_tj import *
from Public.extend import *
from Test_case.Discussion.createDiscussion import *
from Test_case.Discussion.discussionSetting import *

class chatDiscussion(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    #发送文本
    def test_sendMsg(self):
        number = random.randint(0, 1000)
        createDiscussion.test_mainCreateDiscussion(self)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').send_keys("hello world!%s" %number)
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'send').click()
        time.sleep(1)
        try:
            msg = self.driver.find_element_by_xpath("//android.widget.TextView[@text='hello world!%s']" %number)
            self.assertIsNotNone(msg)
            try:
                self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'record_status'))
                AssertionError("文本发送失败")
                raise False
            except:
                pass
            print("文本比对成功")
        except AssertionError as e:
            AssertionError("文本比对失败")
            raise


    #发送图片
    def test_sendPic(self):
        createDiscussion.test_mainCreateDiscussion(self)

        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'pick_image').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.GridView[@resource-id='"+packageName+"pic_gridview']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'btn_send').click()
        time.sleep(1)


        try:
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='"+packageName+"record_content']"))
            try:
                self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'record_status'))
                AssertionError("图片发送失败")
                raise False
            except:
                pass
            print("图片比对成功")
        except AssertionError as e:
            AssertionError("图片发送失败")
            raise

    #发送表情
    def test_sendEmoji(self):
        createDiscussion.test_mainCreateDiscussion(self)

        self.driver.find_element_by_id(packageName + 'radio_emoji').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'send').click()
        time.sleep(1)
        try:
             self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"record_content' and @text='<emoji src=\"smile\"/>']"))
             try:
                 self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'record_status'))
                 AssertionError("表情发送失败")
                 raise False
             except:
                 pass
             print("表情发送成功")
        except AssertionError as e:
            AssertionError("表情发送失败")
            raise

    #@功能
    def test_atSomeone(self):
        createDiscussion.test_mainCreateDiscussion(self)

        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').send_keys("@")
        #跳转界面延迟
        time.sleep(3)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "选择@的人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        short_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'send').click()
        time.sleep(2)
        long_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[10]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        result = long_text.find("%s" %short_text)
        try:
            self.assertNotEqual(result, -1)
            try:
                self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'record_status'))
                AssertionError("@失败")
                raise False
            except:
                pass
            print("@成功")
        except AssertionError as e:
            AssertionError("@失败")
            raise

    #@多人
    def test_atMore(self):
        self.name = publicMethod.get_username(self)
        # 主面板+号创建讨论组
        self.driver.find_element_by_id(packageName + 'action_more').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='创建讨论组']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ExpandableListView[@resource-id='"+packageName+"contact_expandable_list']/android.widget.LinearLayout[8]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]").click()
        time.sleep(2)
        # 点击创建按钮
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(3)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').send_keys("@")
        # 跳转界面延迟
        time.sleep(3)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "选择@的人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'right_tv').text, "确定")
            self.assertEqual(self.driver.find_element_by_id(packageName + 'left_tv').text, "取消")
            pass
        except AssertionError as e:
            AssertionError("无法@多人")
            raise
        short_text1 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        short_text2 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        short_text3 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[5]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[5]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'send').click()
        time.sleep(2)
        long_text = self.driver.find_element_by_id(packageName + 'record_content').text
        result1 = long_text.find("%s" %short_text1)
        result2 = long_text.find("%s" %short_text2)
        result3 = long_text.find("%s" %short_text3)
        try:
            self.assertNotEqual(result1 ,"-1")
            self.assertNotEqual(result2, "-1")
            self.assertNotEqual(result3, "-1")
            try:
                self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'record_status'))
                AssertionError("@多人失败")
                raise False
            except:
                pass
            print("@多人比对成功")
        except AssertionError as e:
            AssertionError("@多人比对失败")
            raise




    #建立视频会议
    def test_videoTalk(self):
        createDiscussion.test_mainCreateDiscussion(self)

        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'videoTalk').click()
        time.sleep(1)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title_bar_text').text, "添加参会者")
        except AssertionError as  e:
            AssertionError("打开添加参会者界面失败")
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id='"+packageName+"user_list']/android.widget.RelativeLayout[2]/android.widget.CheckBox[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'name').text)
            print("建立视频会议成功")
            self.driver.close_app()
        except AssertionError as e:
            AssertionError("建立视频会议失败")


    #发送文件
    def test_sendFile(self):
        createDiscussion.test_mainCreateDiscussion(self)

        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'send_file').click()
        time.sleep(1)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "已选0个")
        except AssertionError as e:
            AssertionError("打开选择文件界面失败")
        self.driver.find_element_by_xpath("//android.widget.ExpandableListView[@resource-id='"+packageName+"file_expandable_list']/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'menu_send').click()
        time.sleep(2)
        #判断是否跳转回讨论组IM界面
        try:
            self.assertIsNotNone(self.driver.find_element_by_id(packageName + 'action_setting'))
            print("发送文件成功")
        except AssertionError as e:
            AssertionError("发送文件失败")


    @classmethod
    def tearDown(self):
        pass