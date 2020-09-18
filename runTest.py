#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/16
# @Version : 1.0

import os
import pytest

# pytest.main()

pytest.main(['--alluredir=reports'])
os.system('allure serve reports')
