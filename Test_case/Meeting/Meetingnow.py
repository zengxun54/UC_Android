# -*- encoding:utf-8 -*-

import unittest
from appium import webdriver
import os
import time
import configparser

class Meetingnow (unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_cups = {}
        # 设备平台
        desired_cups['platformName'] = 'Android'
        # 设备系统版本
        desired_cups['platformVersion'] = '8.0.0'
        # 设备名称
        desired_cups['deviceName'] = 'SJE0217421000430'
        # apk安装包路径
        PATH = lambda p: os.path.abspath (os.path.join (os.path.dirname (__file__), p))
        desired_cups['app'] = PATH (r'C:\Users\yl1477\Desktop\Yealink_UC_Android_1.0.295.1010-local-release.apk')
        # 启动app
        self.driver = webdriver.Remote ('http://localhost:4723/wd/hub', desired_cups)
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        time.sleep (10)
    @classmethod
    def tearDown(self):
        pass
    def test_1meetingnow(self):
        conf = configparser.ConfigParser ()
        conf.read ("../../config/parameters.ini", encoding='utf-8')
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
        conf.read ("./config/parameters.ini", encoding='utf-8')
        self.driver.find_element_by_id ('com.yealink.uc.android:id/name').click ()  # 点击通话保密图标
        self.driver.find_element_by_id('com.yealink.uc.android:id/invite').click()#邀请
        self.driver.find_element_by_id ('com.yealink.uc.android:id/bs_blank').click ()#邀请联系人

        self.driver.find_element_by_id ('com.yealink.uc.android:id/contact_search').send_keys ('tj')
        time.sleep (3)
        self.driver.find_element_by_name ('汤葭').click ()
        time.sleep (2)
        self.driver.find_element_by_id ('com.yealink.uc.android:id/right_tv').click ()
        # time.sleep (20)
        # self.driver.find_element_by_id ('com.yealink.uc.android:id/name').click ()  # 点击通话保密图标
        self.driver.find_element_by_id ('com.yealink.uc.android:id/more').click ()
        self.driver.find_element_by_name ('成员列表').click ()
        list=['成员列表','主持人(1)','刘博琛','全部禁言','锁定会议']
        source = self.driver.page_source
        for a in list:
            el=a
            try:
                assert el in source
            except Exception as msg:
                print ('成员界面显示异常！')
                raise 'Fail'  # 抛出异常这个用例就不会pass了


if __name__== '__main__':
    unittest.main ()