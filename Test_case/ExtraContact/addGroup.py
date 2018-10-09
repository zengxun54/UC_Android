#Author:Joy Tang
# -*- coding: utf-8 -*-

import unittest
import sys
from appium.webdriver.common.touch_action import TouchAction

sys.path.append("../../")
from Public.publicMethod_tj import *

class addGroup(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    #添加按钮添加
    def test_addGroupByButton(self):
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_external').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'bs_message').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'tv_dialog_title').text, "添加分组")
        except AssertionError as e:
            AssertionError("弹框失败")
            raise
        index = random.randint(0, 1000)
        self.driver.find_element_by_id(packageName + 'edit').send_keys("Group%s" %index)
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        try:
            self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('text(\"Group'+str(index)+' (0)\")'))
            print("添加外部联系人分组成功")
            return index
        except AssertionError as e:
            AssertionError("添加外部联系人分组失败")

    #分组管理添加
    def test_addGroupByGroupManage(self):
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'contact_external').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise

        #长按default
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        TouchAction(self.driver).long_press(el).perform()
        self.driver.find_element_by_id(packageName + 'bs_blank').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "分组管理")
        except AssertionError as e:
            AssertionError("跳转分组管理界面失败")
            raise
        self.driver.find_element_by_android_uiautomator('text(\"添加分组\")').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'tv_dialog_title').text, "添加分组")
        except AssertionError as e:
            AssertionError("弹框失败")
            raise
        index = random.randint(0, 1000)
        self.driver.find_element_by_id(packageName + 'edit').send_keys("Group%s" %index)
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        try:
            self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('text(\"Group'+str(index)+'\")'))
            self.driver.find_element_by_id(packageName + 'right_tv').click()
            time.sleep(2)
            try:
                self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('text(\"Group' + str(index) + ' (0)\")'))
            except AssertionError as e:
                AssertionError("添加外部联系人分组失败")
            print("添加外部联系人分组成功")
        except AssertionError as e:
            AssertionError("添加外部联系人分组失败")


    @classmethod
    def tearDown(self):
        pass
