#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
import time
import unittest

sys.path.append("../../")
from Public.publicMethod_tj import *


class createDiscussion(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    #主界面创建
    def test_mainCreateDiscussion(self):
        self.name = publicMethod.get_username(self)
        #主面板+号创建讨论组
        self.driver.find_element_by_id(packageName + 'action_more').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='创建讨论组']").click()
        time.sleep(2)

        #添加成员
        self.driver.find_element_by_id(packageName + 'contact_search').clear()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'contact_search').send_keys("林美霞")
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_child_item').click()
        time.sleep(2)

        #点击创建按钮
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(3)

        #结果比对
        try:
            #提示语比对
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"record_content' and @text='讨论组创建成功！']")
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"record_content' and @text='您邀请林美霞加入本讨论组']")
            try:
                #默认名称比对
                discussionName = self.driver.find_element_by_id(packageName + 'title_bar_text').text
                discussionName1 = ("%s,林美霞" %(self.name))
                result = self.assertEqual(discussionName, discussionName1)
                memberCount = self.driver.find_element_by_id(packageName + 'title_member_count').text
                result1 = self.assertEqual(memberCount, "(2)")
            except AssertionError as e:
                AssertionError("创建失败")
                raise
            print("讨论组创建比对成功")
        except AssertionError as e:
            AssertionError("讨论组创建失败")
            raise

    #IM单人聊天创建
    def test_ImCreateDiscussion(self):
        self.name = publicMethod.get_username(self)

        #搜索一个人，进入IM聊天界面
        self.driver.find_element_by_id(packageName + 'action_search').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'edit').clear()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'edit').send_keys("陈海城")
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_send_message').click()
        time.sleep(2)

        #聊天设置，添加新成员
        self.driver.find_element_by_id(packageName + 'action_setting').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'start_chat').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_search').send_keys("王美凤")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"contact_screen_name' and @text='王美凤']").click()
        time.sleep(2)

        # 点击创建
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(3)

        #结果比对
        try:
            #提示语比对
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"record_content' and @text='讨论组创建成功！']")
            self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='"+packageName+"record_content' and @text='您邀请陈海城、王美凤加入本讨论组']")
            try:
                #默认名称比对
                discussionName = self.driver.find_element_by_id(packageName + 'title_bar_text').text
                discussionName1 = ("%s,陈海城,王美凤" %(self.name))
                self.assertEqual(discussionName, discussionName1)
                memberCount = self.driver.find_element_by_id(packageName + 'title_member_count').text
                self.assertEqual(memberCount, "(3)")
            except AssertionError as e:
                AssertionError("创建失败")
                raise
            print("讨论组默认名称比对成功")
        except AssertionError as e:
            AssertionError("创建失败")
            raise



    @classmethod
    def tearDown(self):
        pass
if __name__== '__main__':
    unittest.main(verbosity=2)




