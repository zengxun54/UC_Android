#!/usr/bin/env python
#coding = utf-8
__author__ = 'liujx'

import time
import sys
import importlib

importlib.reload(sys)
import time, os

class Action(object):
    """
    savepng封装所有页面都公用的方法，例如截图/获取当前时间
    """

    # saveScreenshot:通过图片名称，进行截图保存
    def saveScreenshot(self, driver, name):
        """
        快照截图
        name:图片名称
        """
        image = driver.save_screenshot(self.savePngName(name))
        return image

    # savePngName:生成图片的名称
    def savePngName(self, name):
        """
        name：自定义图片的名称
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "..\\report\\"
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            filename = str(fp) + "\\" + str(tm) + str("_") + str(name) + str(type)
            print(filename)
            return filename
        else:
            os.makedirs(fp)
            filename = str(fp) + "\\" + str(tm) + str("_") + str(name) + str(type)
            print(filename)
            return filename


    #获取系统当前时间
    def saveTime(self):
        """
        返回当前系统时间以括号中（2014-08-29-15_21_55）展示
        """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))