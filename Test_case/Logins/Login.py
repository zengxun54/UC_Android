# -*- encoding:utf-8 -*-
__author__ = 'zhonghaitao'
import unittest
from appium import webdriver
import time
import config_factory
import Const


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config_factory=config_factory.ConfigFactory()
        print('setup')
        # 启动app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.config_factory.desired_cups)
        # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        time.sleep(3)
        # 检查是否有系统权限弹窗
        self.config_factory.always_allow(self.driver,3)

    @classmethod
    def tearDownClass(self):
        print('tearDown')
        # pass

    # @unittest.skip("demonstrating skipping")
    # def test_first_install_welcome(self):
    #     '''
    #     首次安装进入的是引导页
    #
    #     '''
    #     #等待欢迎页面出现
    #     self.driver.wait_activity('com.yealink.uc.android.login.WelcomeActivity',2,2)
    #     #向右滑动3张引导图
    #     self.config_factory.swipeToRight(self.driver,200,3)
    #     # 点击立即体验按钮
    #     self.config_factory.find_element_id(self.driver,Const.EXPETIENCE).click()
    #
    # def test_login_checkui(self):
    #     '''
    #         正常用例：校验ui
    #         检查点：页面元素，值
    #     '''
    #     self.driver.wait_activity("com.yealink.uc.android.login.LoginActivity",2,2)
    #     #用户名
    #     username=self.config_factory.find_element_id(self.driver,Const.USERNAME).text
    #     #密码
    #     password=self.config_factory.find_element_id(self.driver,Const.PASSWORD).text
    #     #服务器
    #     server=self.config_factory.find_element_id(self.driver,Const.SERVER).text
    #     #记住密码
    #     ckb_remember_psw=self.config_factory.find_element_id(self.driver,Const.REMENBERPASSWORD).get_attribute("checked")
    #
    #     #忘记密码
    #     # forgetpassword=self.config_factory.find_element_id(self.driver,Const.FORGETPASSWORD).text
    #     #意见反馈
    #     feedback=self.config_factory.find_element_id(self.driver,Const.FEEDBACK).text
    #     #校验默认值
    #     self.assertEqual(username,"",msg="用户名输入框默认值不对")
    #     self.assertEqual(password,"",msg="密码默认值不对")
    #     self.assertEqual(server,"ume.yealink.com",msg="服务器默认值不对")
    #     self.assertTrue(ckb_remember_psw, msg="默认选中状态不对")
    #     # self.assertEqual(forgetpassword,"忘记密码",msg="忘记密码文案错误")
    #     self.assertEqual(feedback,"意见反馈",msg="意见反馈文案错误")
    #     # self.assertTrue(self.config_factory.find_element_id(self.driver,Const.FORGETPASSWORD).get_attribute("Clickable"),"忘记密码不能点击")
    #     self.assertTrue(self.config_factory.find_element_id(self.driver,Const.FEEDBACK).get_attribute("Clickable"),"意见反馈不能点击")

    # def test_login_errorhost(self):
    #     '''
    #         异常用例：输入错误的服务器地址
    #         检查点：错误提示是否正确
    #     '''
    #     #输入数据进行登录操作
    #     self.config_factory.login(self.driver,self.config_factory.login_errorhost["username"],self.config_factory.login_errorhost["password"],self.config_factory.login_errorhost["server"])
    #     #校验提示
    #     self.config_factory.asserttips(self.driver,self.config_factory.login_errorhost["title"],self.config_factory.login_errorhost["message"])
    #
    # def test_login_errorusername(self):
    #     '''
    #         异常用例：输入错误的用户名
    #         检查点：错误提示是否正确
    #     '''
    #     # 输入数据进行登录操作
    #     self.config_factory.login(self.driver, self.config_factory.login_errorusername["username"],self.config_factory.login_errorusername["password"],self.config_factory.login_errorusername["server"])
    #     # 校验提示
    #     self.config_factory.asserttips(self.driver, self.config_factory.login_errorusername["title"],self.config_factory.login_errorusername["message"])
    #
    # def test_login_notexistusername(self):
    #     '''
    #         异常用例：输入不存在的用户名
    #         检查点：错误提示是否正确
    #     '''
    #     # 输入数据进行登录操作
    #     self.config_factory.login(self.driver, self.config_factory.login_notexistusername["username"],self.config_factory.login_notexistusername["password"],self.config_factory.login_notexistusername["server"])
    #     # 校验提示
    #     self.config_factory.asserttips(self.driver, self.config_factory.login_notexistusername["title"],self.config_factory.login_notexistusername["message"])
    #
    # def test_login_errorpassword(self):
    #     '''
    #         异常用例：输入错误的密码
    #         检查点：错误提示是否正确
    #     '''
    #     # 输入数据进行登录操作
    #     self.config_factory.login(self.driver, self.config_factory.login_errorpassword["username"],self.config_factory.login_errorpassword["password"],self.config_factory.login_errorpassword["server"])
    #     # 校验提示
    #     self.config_factory.asserttips(self.driver, self.config_factory.login_errorpassword["title"],self.config_factory.login_errorpassword["message"])

    # def test_login_nullhost(self):
    #     '''
    #         异常用例：服务器地址为空
    #         检查点：错误提示是否正确
    #     '''
    #     # 输入数据进行登录操作
    #     self.config_factory.login(self.driver, self.config_factory.login_nullhost["username"],self.config_factory.login_nullhost["password"],self.config_factory.login_nullhost["server"])
    #     # 校验提示
    #     self.config_factory.asserttips(self.driver, self.config_factory.login_nullhost["title"],self.config_factory.login_nullhost["message"])

    def test_login_zq(self):
        '''
            正常用例：输入的数据都正确
            检查点：登录是否成功
        '''
        # 输入数据进行登录操作
        self.config_factory.login(self.driver, self.config_factory.login_zq["username"],self.config_factory.login_zq["password"],self.config_factory.login_zq["server"])

        #日程权限
        self.config_factory.always_allow(self.driver,3)
        #校验当前activity是否为mainactivity
        self.assertEqual(self.driver.current_activity,'com.yealink.uc.android.MainActivity',msg="未登录成功")


if __name__== '__main__':
     unittest.main ()