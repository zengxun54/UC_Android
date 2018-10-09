#Author:Joy Tang
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")
from Test_case.ExtraContact.addGroup import *

class delGroup(unittest.TestCase):
    def setUp(self):
        self.driver = publicMethod.open_app(self)
    def test_delGroup(self):
        #先添加一个分组
        index1 = addGroup.test_addGroupByButton(self)
        # 长按default
        el = self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        TouchAction(self.driver).long_press(el).perform()
        self.driver.find_element_by_id(packageName + 'bs_blank').click()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.find_element_by_id(packageName + 'title').text, "分组管理")
        except AssertionError as e:
            AssertionError("跳转分组管理界面失败")
            raise
        self.driver.find_element_by_android_uiautomator('text(\"Group'+str(index1)+'\")').click()
        time.sleep(2)
        self.driver.find_element_by_id(packageName + 'button_ok').click()
        time.sleep(2)
        source = self.driver.page_source
        el = 'Group'+str(index1)
        if el.find(source) == -1:
            self.driver.find_element_by_id(packageName + 'right_tv').click()
            time.sleep(2)
            source1 = self.driver.page_source
            if el.find(source1) == -1:
                print("删除分组成功")
            else:
                return False
        else:
            return False



    @classmethod
    def tearDown(self):
        pass