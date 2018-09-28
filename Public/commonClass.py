# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time,configparser
import re
debug_id_pre = 'com.yealink.uc.android:id/'
# conf_url = "../../config/config.ini"#单个运行
# param_url = "../../config/parameters.ini"#单个运行
conf_url = "config/config.ini"#单个运行
param_url = "config/parameters.ini"#单个运行
class commonCase(unittest.TestCase):
    def __init__(self,debug_id_pre):
        self.debug_id_pre = debug_id_pre
        self.conf = configparser.ConfigParser()
        # conf_url = "../../config/config.ini"#单个运行
        # param_url = "../../config/config.ini"#单个运行
        # conf_url = "config/config.ini"#全部运行
        # param_url = "config/config.ini"#全部运行
        self.conf.read(conf_url,encoding='utf-8')#单个运行
        # self.conf.read("config/config.ini",encoding='utf-8')#全部运行
        self.paramter = configparser.ConfigParser()
        self.paramter.read(param_url,encoding='utf-8')#单个运行
        # self.paramter.read("config/parameters.ini",encoding='utf-8')#全部运行
    def startUpApp(self):
        desired_cups = {}
        # 设备平台 case_dir = conf.get("测试用例路径", "用例路径")
        desired_cups['platformName'] = self.conf.get("Appium", "platformName")
        # 设备系统版本
        desired_cups['platformVersion'] = self.conf.get("Appium", "platformVersion")
        # 设备名称
        desired_cups['deviceName'] = self.conf.get("Appium", "deviceName")
        # apk安装包路径
        PATH = lambda p: os.path.abspath(os.path.join (os.path.dirname (__file__), p))
        desired_cups['app'] = PATH(self.conf.get("Appium", "appPackage"))
        desired_cups['appWaitActivity'] = self.conf.get("Appium", "appWaitActivity")
        desired_cups['noReset'] = True
        # 启动app
        # print(self.conf.get("Appium", "url"))
        # exit(0)
        driver = webdriver.Remote(self.conf.get("Appium", "url"), desired_cups)
        time.sleep(20)
        return driver
    #@拨号盘点击
    def test_click_num(self,driver,call_str):
        debug_id_pre = self.debug_id_pre
        for x in call_str:
            if x == '1':
                driver.find_element_by_id(debug_id_pre+'one').click()
                time.sleep(1)
            elif x == '2':
                driver.find_element_by_id(debug_id_pre+'two').click()
                time.sleep(1)
            elif x == '3':
                driver.find_element_by_id(debug_id_pre+'three').click()
                time.sleep(1)
            elif x == '4':
                driver.find_element_by_id(debug_id_pre+'four').click()
                time.sleep(1)
            elif x == '5':
                driver.find_element_by_id(debug_id_pre+'five').click()
                time.sleep(1)
            elif x == '6':
                driver.find_element_by_id(debug_id_pre+'six').click()
                time.sleep(1)
            elif x == '7':
                driver.find_element_by_id(debug_id_pre+'seven').click()
                time.sleep(1)
            elif x == '8':
                driver.find_element_by_id(debug_id_pre+'eight').click()
                time.sleep(1)
            elif x == '9':
                driver.find_element_by_id(debug_id_pre+'nine').click()
                time.sleep(1)
            elif x == '.':
                driver.find_element_by_id(debug_id_pre+'star').click()
                time.sleep(1)
            elif x == '0':
                driver.find_element_by_id(debug_id_pre+'zero').click()
                time.sleep(1)
            elif x == '#':
                driver.find_element_by_id(debug_id_pre+'pound').click()
                time.sleep(1)
    #@获取第一条通话记录的信息
    def get_first_calllog_info(self,driver,info_type):
        debug_id_pre = self.debug_id_pre
        time.sleep(1)
        lv_contact_log = driver.find_element_by_id(debug_id_pre+'lv_contact_log')
        #获取通话记录集合
        calllog_set = lv_contact_log.find_elements_by_class_name("android.widget.RelativeLayout")
        #获取第一条通话记录的名字或通话类型
        calllog_first_info = calllog_set[1].find_element_by_id(debug_id_pre+info_type).get_attribute('text')
        #获取第一条通话记录的记录数
        if info_type == 'call_log_name':
            calllog_first_counter_list = re.findall('\((.*?)\)', calllog_first_info)
            if len(calllog_first_counter_list) == 0:
                calllog_first_counter = 1
            else:
                calllog_first_counter = int(calllog_first_counter_list[0])
            return calllog_first_counter
        elif info_type == 'call_log_protocol':
            return calllog_first_info
    #@获取通话记录总数
    def get_calllog_counter(self,driver):
        debug_id_pre = self.debug_id_pre
        tv_recent_calllog_title = driver.find_element_by_id(debug_id_pre+'tv_recent_calllog_title')
        calllog_counter = int(tv_recent_calllog_title.get_attribute('text')[5:-1])
        return int(calllog_counter)
    #@挂断通话
    def hang_up(self,driver):
        print('hang up')
        debug_id_pre = self.debug_id_pre
        # com.yealink.uc.android.alpha:id/left_btn
        time.sleep(5)
        driver.find_element_by_id(debug_id_pre+'name').click()#通话界面图标
        time.sleep(1)
        clickRes = driver.find_element_by_id(debug_id_pre+'hangup').click()#挂断通话
    #@获取通话统计的分辨率及帧率
    def get_resolution_and_fps(self,driver):#获取通话统计的分辨率及帧率
        resolution = driver.find_element_by_xpath("//android.widget.TextView[@text='分辨率']/following-sibling::android.widget.TextView")
        resolution_value = resolution.get_attribute('text')
        fps = driver.find_element_by_xpath("//android.widget.TextView[@text='帧率']/following-sibling::android.widget.TextView")
        fps_value = fps.get_attribute('text')#16 fps
        print(fps_value)
        if resolution_value == '0*0' or fps_value == '0 fps':
            return False
        return True
    def call_num(self,driver,call_num_str):
        time.sleep(20)
        print('call_num')
        driver.find_element_by_name('拨号').click()
        time.sleep(3)
        self.test_click_num(driver,call_num_str)
        time.sleep(1)
        # 点击拨号
        driver.find_element_by_id(debug_id_pre+self.paramter.get("dialPlate", "call_send_xpath")).click()
        time.sleep(3)
        driver.find_element_by_id(debug_id_pre+self.paramter.get("dialPlate", "call_whose_name")).click()#判断通话界面图标是否出现
        time.sleep(2)
        source = driver.page_source
        el = (debug_id_pre+self.paramter.get("dialPlate", "call_whose_name"))
        if el in source:
            return True
        return False
    def result_handler(self,result,error):
        try:
            assert result
        except Exception:
            raise(error)
    def get_conf(self,option,value):
        paramter = self.debug_id_pre+self.paramter.get(option,value)
        return paramter
    def restart_adb(self):
        kill_adb_cmd = 'adb kill-server'
        start_adb_cmd = 'adb start-server'
        # os.chdir(retval+module_dir)
        # time.sleep(10)
        if not (os.system(kill_adb_cmd)==0):
            os.system(kill_adb_cmd)#不成功就启动
        print('success')
        # os.system(start_adb_cmd)#成功就启动
