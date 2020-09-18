#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/16
# @Version : 1.0

import pytest
from pages.loginPage import LoginPage
from case_data.login_data import LoginData
from common.logger import log


class TestLogin:
    """登陆测试用例"""
    @pytest.mark.parametrize('case', LoginData.success_data)
    def test_login_success(self, case, login_fixture):
        """登陆成功测试"""
        login_page, index_page = login_fixture
        login_page.login(case['username'], case['password'])
        res = index_page.if_login_success()
        try:
            assert "登陆成功" == res
        except AssertionError as e:
            log.error("成功登陆用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("登陆成功用例执行成功")
            index_page.logout()
