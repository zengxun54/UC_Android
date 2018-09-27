# coding=utf-8
__author__ = 'zhonghaitao'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import Const
APP_URL="com.yealink.uc.android.alpha:id/"

class ConfigFactory(object):
    # ------------------------------------------------------------------------
    #配置
    # desired_cups={
    #     "platformName": "Android",
    #     "platformVersion": "6.0",
    #     "deviceName": "69DDU16513003941",
    #     "appWaitActivity": "com.yealink.uc.android.login.LoginActivity",
    #     "noReset": "True",
    #     "app": r"F://Yealink_UC_Android_1.1.3.839-pre-debug.apk",
    # }
    desired_cups={
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": "8452f49e0804",
        "appWaitActivity": "com.yealink.uc.android.login.LoginActivity",
        "noReset": "True",
        "app": r"F:\UME android apk\Yealink_UC_Android_1.1.11.1018-local-release.apk",
    }

    # ------------------------------------------------------------------------
    #用例数据
    login_errorhost={
        "username":  "yl1872@yealink.com",
        "password" : "Zhht@080",
        "server" : "sjsjsj",
        "title":"登录失败",
        "message":"连接服务器失败，请检查网络或者服务器地址！"
    }
    login_errorusername={
        "username": "d",
        "password": "Zhht@080",
        "server": "ume.yealink.com",
        "title": "登录失败",
        "message": "用户名或密码错误"
    }
    login_notexistusername = {
        "username": "ddsdsdsds",
        "password": "Zhht@080",
        "server": "ume.yealink.com",
        "title": "登录失败",
        "message": "没有找到对应账号"
    }
    login_errorpassword = {
        "username": "yl1872@yealink.com",
        "password": "Zhht@081",
        "server": "ume.yealink.com",
        "title": "登录失败",
        "message": "用户名或密码错误，请重新输入"
    }
    login_nullhost = {
        "username": "yl1872@yealink.com",
        "password": "Zhht@080",
        "server": "",
        "title": "登录失败",
        "message": "服务器地址不能为空"
    }
    login_zq = {
        "username": "cs334@uctest.yealink.com",
        "password": "6rE!xVLd",
        "server": "uctest.yealink.com",
    }


    # ------------------------------------------------------------------------
    #封装方法
    #首次安装后进入应用的权限弹窗处理
    def always_allow(self,driver,number):
        # 判断是否有权限弹窗,number为判断弹窗次数
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(driver, 1, 1).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    #向右滑动
    def swipeToRight( self,driver, during, num) :
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        for i in range(num):
            driver.swipe(x * 6 / 7 , y / 2 , x / 7 , y / 2 , during)
            time.sleep(4)

    #向左滑动
    def swipeToLeft( self,driver, during, num) :
        print(driver.get_window_size())
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        for i in range(num):
            driver.swipe(x / 7 , y / 2 , x * 5 / 7 , y / 2 , during)
            time.sleep(3)
    #针对密码输入框进行清空操作
    def editClear(self,driver, el):
        el.click()
        driver.keyevent(123)
        for i in range(0, 8):
             driver.keyevent(67)

    def find_element_id(self,driver,id):
        element=driver.find_element_by_id(APP_URL+id)
        return element

    def login(self,driver,username,password,server):
        # 赋值
        driver.find_element_by_id(APP_URL + Const.USERNAME).send_keys(username)
        self.editClear(driver, driver.find_element_by_id(APP_URL + Const.PASSWORD))
        driver.find_element_by_id(APP_URL + Const.PASSWORD).send_keys(password)
        driver.find_element_by_id(APP_URL + Const.SERVER).send_keys(server)
        driver.hide_keyboard()  # 隐藏输入法

        # 登录操作
        driver.find_element_by_id(APP_URL + Const.LOGIN).click()
        time.sleep(3)

    def  asserttips(self,driver,title,message):
        # 获取提示值
        title1 = driver.find_element_by_id(APP_URL + Const.FAILTITLE).text
        message1 = driver.find_element_by_id(APP_URL + Const.FAILMESSAGE).text
        # print(message)
        # 校验提示
        if title ==title1.encode("UTF-8"):
            pass
        else:
            raise ("提示标题不正确")
        if message == message1.encode("UTF-8"):
            pass
        else:
            raise ("提示名称不正确")
        # 关闭提示
        driver.find_element_by_id(APP_URL+ Const.FAILBUTTON).click()