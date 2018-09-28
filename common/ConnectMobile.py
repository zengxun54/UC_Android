#!/usr/bin/env python
#coding = utf-8
__author__ = 'liujx'
import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
import uiautomator2 as u2


#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
#app = '' #app包名

# desired_caps = {}
# desired_caps['platformName'] = platformName
# desired_caps['platformVersion'] = platformVersion
# desired_caps['deviceName'] = deviceName
# desired_caps['appPackage'] = appPackage
# desired_caps['appActivity'] = appActivity
# desired_caps['newCommandTimeout']=newCommandTimeout
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动app
#desired_caps['app'] = PATH('C:\\Users\\yl1198\\Downloads\\Yealink_UC_Android_1.0.290.978-pre-debug.apk')　
#time.sleep(5) #启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素

def connectmobile():
    # platformName = 'Android'  # 设备系统
    # platformVersion = '7.1.2'  # 设备系统版本
    # deviceName = 'e43bd0eb'  # 设备名称,通过adb devices获取
    # newCommandTimeout = 300
    # appPackage = 'com.yealink.uc.android.alpha'  # 通过aapt dump badging包名来获取
    # appActivity = 'com.yealink.uc.android.StartActivity'  # 通过aapt dump badging包名来获取
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.1.2',
        'deviceName': 'e43bd0eb',
        'newCommandTimeout': '300',
        'noReset':'true',
        'appPackage': 'com.yealink.uc.android.alpha',
        'appActivity': 'com.yealink.uc.android.StartActivity',
        'automationName':'uiautomator2',
        # 'platformName': 'Android',
        # 'platformVersion': '5.1.1',
        # 'deviceName': '127.0.0.1：62025',
        # 'newCommandTimeout': '300',
        # 'noReset': 'true',
        # 'appPackage': 'com.yealink.uc.android.alpha',
        # 'appActivity': 'com.yealink.uc.android.StartActivity',
        # 'automationName': 'uiautomator2',
    }

    return desired_caps

