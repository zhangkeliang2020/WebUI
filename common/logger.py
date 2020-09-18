#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/14
# @Version : 1.0

import os
import logging
from common.handle_config import conf
from common.basePath import LOG_DIR

log_filepath = os.path.join(LOG_DIR, conf.get("log", "filename"))


class Logger:
    """日志处理模块"""

    # 定义静态方法，可以不用实例化，通过类名直接调用
    @staticmethod
    def creat_logger():
        """
        创建日志收集器
        :return:logger
        """
        # 创建一个日志收集器
        logger = logging.getLogger("zkl")
        # 设置日志等级
        logger.setLevel(conf.get('log', 'level'))
        # 设置输出渠道及输出等级
        # 1、日志写入自定义的log文件
        fh = logging.FileHandler(log_filepath, encoding='utf8')
        fh.setLevel(conf.get('log', 'fh_level'))
        logger.addHandler(fh)

        # 日志标准输出stdout
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log', 'sh_level'))
        logger.addHandler(sh)

        # 创建一个输出格式
        formats = '%(asctime)s --[%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        form = logging.Formatter(formats)

        # 设置各渠道日志输出格式
        fh.setFormatter(form)
        sh.setFormatter(form)

        return logger


log = Logger.creat_logger()
