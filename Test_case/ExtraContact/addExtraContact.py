#Author:Joy Tang
# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("../../")
from Public.publicMethod_tj import *

class addExtraContact(unittest.TestCase):

    def setUp(self):
        self.driver = publicMethod.open_app(self)

    def test_addByHand(self):
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
        self.driver.find_element_by_id(packageName + 'bs_content').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "添加外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        index = random.randint(0, 1000)
        number = random.randint(1000, 10000)
        self.driver.find_element_by_android_uiautomator('text(\"请输入姓名\")').send_keys("自动化%s" %index)
        self.driver.find_element_by_android_uiautomator('text(\"请输入号码\")').send_keys("%s" %number)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        try:
            self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('text(\"自动化'+str(index)+'\")'))
            print("添加外部联系人成功")
            return index
        except AssertionError as e:
            AssertionError("添加外部联系人失败")



    @classmethod
    def tearDown(self):
        pass




