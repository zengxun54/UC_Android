#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")
from Test_case.ExtraContact.addExtraContact import *

class delExtraContact(unittest.TestCase):
    def setUp(self):
        self.driver = publicMethod.open_app(self)

    def test_delExtraContact(self):
        #先添加一个外部联系人
        index = addExtraContact.test_addByHand(self)

        #记录分组下的联系人数量
        text = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        number = text[9:10]
        self.driver.find_element_by_android_uiautomator('text(\"自动化'+str(index)+'\")').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'right_image').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('text(\"编辑\")').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "编辑外部联系人")
        except AssertionError as e:
            AssertionError("跳转界面失败")
            raise
        self.driver.find_element_by_id(packageName + 'btn_delete_contact').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'bs_blank').click()
        time.sleep(2)
        #校验返回到外部联系人界面，且界面没有该成员
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "外部联系人")
            number = int(number) - 1
            self.assertEqual(self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text[9:10], str(number))
            print("删除外部联系人成功")
        except AssertionError as e:
            AssertionError("删除外部联系人失败")
            raise






    @classmethod
    def tearDown(self):
        pass
