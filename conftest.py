#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/16
# @Version : 1.0

import pytest

from selenium import webdriver
from selenium.webdriver import Chrome
from common.handle_config import conf
from common.logger import log
from pages.loginPage import LoginPage
from pages.indexPage import IndexPage


def get_option():
    """
    设置浏览器启动选项
    :return:
    """
    if conf.getboolean('env', 'headless'):  # 判断配置文件中headless参数是否为true
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        opt.add_argument('--no-sandbox')
        return opt
    else:
        return None


@pytest.fixture(scope='class')
def login_fixture():
    """
    登陆前置、后置处理
    :return:
    """
    log.info("开始执行登陆用例！")
    driver = Chrome(options=get_option())
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    driver.quit()
    log.info("登陆用例执行完毕！")






