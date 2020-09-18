#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangkeliang
# @Date    : 2020/8/6
# @Version : 1.0
# from webbrowser import Chrome

from pages.basePage import BasePage
from common.handle_config import conf
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

import time


class LoginPage(BasePage):
    """登陆页面封装"""
    # 通过配置文件读取base_url和登陆页面url,拼接成登陆页面完整的url地址
    url = conf.get('env', 'base_url') + conf.get('url', 'login_url')

    # 登陆的定位器
    usr_name_loc = (By.XPATH, "//input[@name='username']")  # 用户名输入框
    pwd_loc = (By.XPATH, "//input[@name='password']")       # 密码输入框
    lgn_btn_loc = (By.XPATH, "//button[@class='el-button login-btn el-button--primary']")  #登陆按钮
    error_loc = (By.XPATH, "//div[@class='el-form-item__error']")  # 用户或者密码为空提示信息
    alert_loc = (By.XPATH, "//p[@class='el-message__content']")    # 用户名或者密码输入错误弹窗提示信息

    def __init__(self, driver: WebDriver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, username, password):
        self.input_text(self.usr_name_loc, username, "输入用户名")
        self.input_text(self.pwd_loc, password, "输入密码")
        self.click_element(self.lgn_btn_loc, "点击登陆按钮")

    def get_error_info(self):
        """获取登陆失败提示信息"""
        return self.get_element_text(self.error_loc)

    def get_alert_info(self):
        """
        获取登陆失败弹窗信息
        :return:
        """
        return self.get_element_text(self.alert_loc)
