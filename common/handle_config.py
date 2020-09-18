#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/14
# @Version : 1.0

import os
from configparser import ConfigParser
from common.basePath import CONF_DIR


class HandleConfig(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf8")


conf = HandleConfig(os.path.join(CONF_DIR, "config.ini"))
