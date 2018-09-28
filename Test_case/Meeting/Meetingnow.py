# -*- encoding:utf-8 -*-

import unittest
from appium import webdriver
import os
import time
import configparser
from Public import commonClass
class Meetingnow (unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('callRecordCase setup')
        self.call_num_str = '4001'
        # debug_id_pre = 'com.yealink.uc.android.alpha:id/'
        self.commonCls = commonClass.commonCase(commonClass.debug_id_pre)
        self.driver = self.commonCls.startUpApp()
        self.paramter = self.commonCls.paramter
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        # time.sleep(20)
    @classmethod
    def tearDown(self):
        pass
    def test_1meetingnow(self):
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
        self.driver.find_element_by_id (conf.get ("主面板", "更多")).click ()  # 点击加号图标
        time.sleep (3)
        self.driver.find_element_by_name('立即开会').click ()#点击立即会议图标
        time.sleep(3)
        self.driver.find_element_by_id (conf.get ("主面板", "立即视频会议")).click ()
        time.sleep (20)
        # source = self.driver.page_source
        # el = ('com.yealink.uc.android:id/textView')
        # try:
        #     assert el in source
        # except Exception as msg:
        #     print ('失败！')
        #     raise 'Fail'  # 抛出异常这个用例就不会pass了

    def test_2invite(self):
        conf = configparser.ConfigParser ()
        conf.read (commonClass.param_url, encoding='utf-8')
        self.driver.find_element_by_id (commonClass.debug_id_pre+'name').click ()  # 点击通话保密图标
        self.driver.find_element_by_id(commonClass.debug_id_pre+'invite').click()#邀请
        self.driver.find_element_by_id (commonClass.debug_id_pre+'bs_blank').click ()#邀请联系人

        self.driver.find_element_by_id (commonClass.debug_id_pre+'contact_search').send_keys ('tj')
        time.sleep (3)
        self.driver.find_element_by_name ('汤葭').click ()
        time.sleep (2)
        self.driver.find_element_by_id (commonClass.debug_id_pre+'right_tv').click ()
        # time.sleep (20)
        # self.driver.find_element_by_id ('com.yealink.uc.android:id/name').click ()  # 点击通话保密图标
        self.driver.find_element_by_id (commonClass.debug_id_pre+'more').click ()
        self.driver.find_element_by_name ('成员列表').click ()
        list=['成员列表','主持人(1)','刘博琛','全部禁言','锁定会议']
        source = self.driver.page_source
        for a in list:
            el=a
            try:
                assert el in source
            except Exception as msg:
                print ('成员界面显示异常！')
                raise('Fail')  # 抛出异常这个用例就不会pass了


# if __name__== '__main__':
#     unittest.main ()