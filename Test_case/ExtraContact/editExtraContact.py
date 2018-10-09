#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")
from Test_case.ExtraContact.addExtraContact import *
from Test_case.ExtraContact.addGroup import *

class editExtraContact(unittest.TestCase):
    def setUp(self):
        self.driver = publicMethod.open_app(self)

    def test_editExtraContact(self):
        #先添加一个外部联系人
        index = addExtraContact.test_addByHand(self)
        self.driver.find_element_by_android_uiautomator('text(\"自动化' + str(index) + '\")').click()
        time.sleep(2)
        number1 = self.driver.find_element_by_id(packageName + 'item_contact_detail_subtitle').text
        self.driver.find_element_by_id(packageName + 'right_image').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('text(\"编辑\")').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "编辑外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        #新增号码2
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('66668888')
        time.sleep(1)
        #新增邮箱
        self.driver.find_element_by_android_uiautomator('text(\"请输入邮箱\")').send_keys('abc123@qq.com')
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'contact_name').text, '自动化' + str(index) + '')
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, number1)
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, "66668888")
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, "abc123@qq.com")
            print("新增号码2和邮箱成功")
        except AssertionError as e:
            AssertionError("新增号码2和邮箱失败")
            raise

        #移动分组,先新建分组
        self.driver.find_element_by_id(packageName + 'left_btn').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'left_btn').click()
        time.sleep(2)
        index1 = addGroup.test_addGroupByButton(self)
        self.driver.find_element_by_android_uiautomator('text(\"自动化' + str(index) + '\")').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'right_image').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('text(\"编辑\")').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'tv_extra_group_name').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('text(\"Group' + str(index1) + '\")').click()
        time.sleep(1)
        self.driver.find_element_by_id(packageName + 'right_tv').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'contact_name').text, '自动化' + str(index) + '')
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, number1)
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, "66668888")
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").text, "abc123@qq.com")
            self.assertEqual(self.driver.find_element_by_id(packageName + 'contact_department_post').text, 'Group'+str(index1)+'')
            print("移动分组成功")
        except AssertionError as e:
            AssertionError("移动分组失败")
            raise



