#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
import time
import unittest
import random
import uiautomator2 as u2

sys.path.append("../")
from Public.publicMethod_tj import *
from Public.extend import *

class chatDiscussion(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    #发送文本
    def test_sendMsg(self):
        number = random.randint(0, 1000)
        self.driver = publicMethod.open_discussionIm(self)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').send_keys("hello world!%s" %number)
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send').click()
        time.sleep(1)
        try:
            msg = self.driver.find_element_by_xpath("//android.widget.TextView[@text='hello world!%s']" %number)
            self.assertIsNotNone(msg)
            try:
                self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_status'))
                AssertionError("发送失败")
                raise False
            except:
                pass
            print("比对成功")
        except AssertionError as e:
            AssertionError("比对失败")
            raise


    #发送图片
    def test_sendPic(self):
        self.driver = publicMethod.open_discussionIm(self)

        # 先刷屏把有照片的顶走避免干扰
        publicMethod.shuaping(self)

        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/pick_image').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.GridView[@resource-id='com.yealink.uc.android.alpha:id/pic_gridview']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/btn_send').click()
        time.sleep(1)


        try:
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.yealink.uc.android.alpha:id/record_content']"))
            try:
                self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_status'))
                AssertionError("发送失败")
                raise False
            except:
                pass
            print("比对成功")
        except AssertionError as e:
            AssertionError("发送失败")
            raise

    #发送表情
    def test_sendEmoji(self):
        self.driver = publicMethod.open_discussionIm(self)

        # 先刷屏把有文本和照片的顶走避免干扰
        publicMethod.shuaping(self)

        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/radio_emoji').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send').click()
        time.sleep(1)
        try:
             self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.yealink.uc.android.alpha:id/record_content' and @text='<emoji src=\"smile\"/>']"))
             try:
                 self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_status'))
                 AssertionError("发送失败")
                 raise False
             except:
                 pass
             print("比对成功")
        except AssertionError as e:
            AssertionError("发送失败")
            raise

    #@功能
    def test_atSomeone(self):
        self.driver = publicMethod.open_discussionIm(self)

        # 先刷屏把有文本和照片的顶走避免干扰
        publicMethod.shuaping(self)

        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').send_keys("@")
        #跳转界面延迟
        time.sleep(3)
        try:
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title').text, "选择@的人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        short_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send').click()
        time.sleep(2)
        long_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[10]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        result = long_text.find("%s" %short_text)
        try:
            self.assertNotEqual(result, -1)
            try:
                self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_status'))
                AssertionError("发送失败")
                raise False
            except:
                pass
            print("比对成功")
        except AssertionError as e:
            AssertionError("比对失败")
            raise

    #@多人
    def test_atMore(self):
        self.name = publicMethod.get_username(self)
        # 主面板+号创建讨论组
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_more').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='创建讨论组']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ExpandableListView[@resource-id='com.yealink.uc.android.alpha:id/contact_expandable_list']/android.widget.LinearLayout[8]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]").click()
        time.sleep(2)
        # 点击创建按钮
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').send_keys("@")
        # 跳转界面延迟
        time.sleep(3)
        try:
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title').text, "选择@的人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').text, "确定")
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/left_tv').text, "取消")
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
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send').click()
        time.sleep(2)
        long_text = self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_content').text
        result1 = long_text.find("%s" %short_text1)
        result2 = long_text.find("%s" %short_text2)
        result3 = long_text.find("%s" %short_text3)
        try:
            self.assertNotEqual(result1 ,"-1")
            self.assertNotEqual(result2, "-1")
            self.assertNotEqual(result3, "-1")
            try:
                self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/record_status'))
                AssertionError("发送失败")
                raise False
            except:
                pass
            print("比对成功")
        except AssertionError as e:
            AssertionError("比对失败")
            raise




    #建立视频会议
    def test_videoTalk(self):
        self.driver = publicMethod.open_discussionIm(self)

        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/videoTalk').click()
        time.sleep(1)
        try:
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title_bar_text').text, "添加参会者")
        except AssertionError as  e:
            AssertionError("打开添加参会者界面失败")
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id='com.yealink.uc.android.alpha:id/user_list']/android.widget.RelativeLayout[2]/android.widget.CheckBox[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/right_tv').click()
        time.sleep(2)
        try:
            self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/name').text)
            print("建立视频会议成功")
        except AssertionError as e:
            AssertionError("建立视频会议失败")


    #发送文件
    def test_sendFile(self):
        self.driver = publicMethod.open_discussionIm(self)

        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/radio_more').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/send_file').click()
        time.sleep(1)
        try:
            self.assertEqual(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/title').text, "已选0个")
        except AssertionError as e:
            AssertionError("打开选择文件界面失败")
        self.driver.find_element_by_xpath("//android.widget.ExpandableListView[@resource-id='com.yealink.uc.android.alpha:id/file_expandable_list']/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/menu_send').click()
        time.sleep(2)
        #判断是否跳转回讨论组IM界面
        try:
            self.assertIsNotNone(self.driver.find_element_by_id('com.yealink.uc.android.alpha:id/action_setting'))
            print("发送文件成功")
        except AssertionError as e:
            AssertionError("发送文件失败")


    @classmethod
    def tearDown(self):
        pass