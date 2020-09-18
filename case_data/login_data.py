#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/16
# @Version : 1.0


class LoginData:
    success_data = [
        {'username': 'zkl', 'password': 'Zkl@20161234', 'expected': '登陆成功'},
        {'username': 'test012', 'password': 'Zkl@123456789012345678901234567890', 'expected': '登陆成功'}
    ]
    null_data = [
        {'username': '', 'password': 'Zkl@20161234', 'expected': '请输入用户名'},
        {'username': 'zkl', 'password': '', 'expected': '请输入密码'}
    ]

    error_data = [
        {'username': '111', 'password': 'Zkl@20161234', 'expected': '找不到用户'},
        {'username': 'zkl', 'password': '111', 'expected': '密码错误'}
    ]
