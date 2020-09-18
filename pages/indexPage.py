#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/16
# @Version : 1.0


from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class IndexPage(BasePage):
    """首页封装"""
    welcome_loc = (By.XPATH, "//a[contains(text(),'欢迎页')]")

    caret_bottom_loc = (By.XPATH, "//i[@class='el-icon-caret-bottom']")  # 右上角下拉框
    quit_loc = (By.XPATH, "//span[contains(text(),'退出')]")
    modify_pw_loc = (By.XPATH, "//span[contains(text(),'密码修改')]")

    def if_login_success(self):
        """
        判断是否登陆成功
        :return:
        """
        try:
            self.get_element(self.welcome_loc, "查找欢迎页")
        except:
            return "登陆失败"
        else:
            return "登陆成功"

    def logout(self):
        """
        退出登陆
        :return:
        """
        # 点击下拉框
        self.click_element(self.caret_bottom_loc, "点击下拉箭头")
        self.wait_element_clickable(self.quit_loc, "等待退出按钮可点击")
        self.click_element(self.quit_loc, "点击退出")
