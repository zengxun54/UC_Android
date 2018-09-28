#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
import unittest
import random
import time
import re
from Test_case.Discussion.createDiscussion import *

sys.path.append("../../")
from Public.publicMethod_tj import *

class discussionSetting(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    #修改讨论组名称
    def test_changeDiscussionName(self):
        createDiscussion.test_mainCreateDiscussion(self)
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'tv_group_name').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'personal_detail_edit').clear()
        time.sleep(2)
        number = random.randint(0, 1000)
        self.driver.find_element_by_id(packageName + 'personal_detail_edit').send_keys("自动化修改讨论组名称%d" %number)
        time.sleep(2)

        #修改名称文本框字数统计比对
        lenth = len("自动化修改讨论组名称%d" %number)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName +'personal_detail_edit_length_tip').text, (100-lenth))
        except AssertionError as e:
            AssertionError("讨论组名称字数统计错误")

        #修改后点击保存按钮
        self.driver.find_element_by_id(packageName + 'btn_confirm').click()
        time.sleep(2)

        #获取新的讨论组名字，与设定的值进行比较
        new_name = self.driver.find_element_by_id(packageName + 'tv_group_name').text
        try:
            self.assertEqual("自动化修改讨论组名称%d" %number, new_name)
        except AssertionError as e:
            AssertionError("修改讨论组名称失败")

        #返回讨论组界面比对title和提示语
        self.driver.find_element_by_id(packageName + 'left_btn').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title_bar_text').text, new_name)
        except AssertionError as e:
            AssertionError("修改讨论组提示语错误")

    #添加成员
    def test_addMember(self):
        createDiscussion.test_mainCreateDiscussion(self)
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_search').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'contact_search').send_keys("梁欣")
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='"+packageName+"contact_child_item']").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").text,"梁欣")
            self.assertEqual(self.driver.find_element_by_id(packageName + 'tv_member_count').text,"查看5人")
            self.driver.find_element_by_id(packageName + 'left_btn').click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title_member_count').text,"(5)")
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]").text, "您邀请梁欣加入本讨论组")
            print("添加成员成功")
        except AssertionError as e:
            AssertionError("添加成员失败")

    #删除单个成员
    def test_delOneMember(self):
        createDiscussion.test_mainCreateDiscussion(self)
        #先加人再删除
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_search').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'contact_search').send_keys("梁欣")
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='"+packageName+"contact_child_item']").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        #删除
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        del_name = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'right_tv').text,"删除(1)")
        except AssertionError as e:
            AssertionError("删除成员计数错误")
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'tv_member_count').text, "查看2人")
            self.assertNotEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text, del_name)
            self.assertNotEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]").text, del_name)
            print("删除成员成功")
        except AssertionError as e:
            AssertionError("比对失败")


    def test_delMoreMember(self):
        createDiscussion.test_mainCreateDiscussion(self)
        # 先加人再删除
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_search').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'contact_search').send_keys("梁欣")
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='"+packageName+"contact_child_item']").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'et_select_member_search').send_keys("刘博琛")
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@resource-id='"+packageName+"contact_child_item']").click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='"+packageName+"llyt_member_container']/android.widget.LinearLayout[6]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        del_name1 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        del_name2 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[5]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[5]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(1)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'right_tv').text,"删除(2)")
        except AssertionError as e:
            AssertionError("删除成员计数错误")
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'tv_member_count').text,"查看2人")
            self.assertNotEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]").text,del_name1)
            self.assertNotEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]").text,del_name2)
            print("删除成员成功")
        except AssertionError as e:
            AssertionError("比对失败")

    #会话置顶
    def test_stick(self):
        # 先进行单人IM，不让讨论组的会话在顶上
        self.driver.find_element_by_id(packageName + 'action_search').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'edit').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'edit').send_keys("林美霞")
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'contact_send_message').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'chat_bar_editor').send_keys("置顶用")
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'send').click()
        time.sleep(2)
        self.driver.close_app()

        self.driver = publicMethod.open_app(self)
        publicMethod.open_discussionSetting(self)
        group_name = self.driver.find_element_by_id(packageName + 'tv_group_name').text
        text = self.driver.find_element_by_id(packageName + 'switch_top').text

        if text == "开启":
            #查看当前是否已经置顶，如果已经置顶了，就验证是否在顶部
            self.driver.find_element_by_id(packageName + 'left_btn').click()
            time.sleep(2)
            self.driver.find_element_by_id(packageName + 'left_btn').click()
            time.sleep(2)
            first_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
            same_group = group_name.find("%s" %first_text[0:5])
            try:
                self.assertNotEqual(same_group, "-1")
                raise False
            except:
                print("当前讨论组已经置顶了")
                pass

        elif text == "关闭":

            self.driver = publicMethod.open_app(self)
            publicMethod.open_discussionSetting(self)
            self.driver.find_element_by_id(packageName + 'switch_top').click()
            time.sleep(1)
            try:
                self.assertEqual(self.driver.find_element_by_id(packageName + 'switch_top').text, "开启")
                print("讨论组置顶成功")
            except AssertionError as e:
                AssertionError("打开置顶开关失败")
                raise False

            #查看当前是否已经置顶
            self.driver.find_element_by_id(packageName + 'left_btn').click()
            time.sleep(2)
            self.driver.find_element_by_id(packageName + 'left_btn').click()
            time.sleep(2)
            first_text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
            same_group = group_name.find("%s" %first_text[0:5])
            try:
                self.assertNotEqual(same_group, "-1")
                raise False
            except:
                print("当前讨论组已经置顶了")
        else:
            raise False


    #设置特别关注
    def test_favorite(self):
        createDiscussion.test_mainCreateDiscussion(self)
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'switch_frequent_contact').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'switch_frequent_contact').text,"开启")
            print("设置特别关注成功")
        except AssertionError as e:
            AssertionError("设置特别关注失败")
            raise False


    def test_quitDiscussion(self):
        createDiscussion.test_mainCreateDiscussion(self)
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width/2, height*7/8, width/2, height/2, 1000)
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'btn_quit_talk_group').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        #退出后回到主界面
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text,"消息")
            print("退出讨论组成功")
        except AssertionError as e:
            AssertionError("退出讨论组失败")

    @classmethod
    def tearDown(self):
        pass







