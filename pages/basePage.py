#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zhangkeliang
# @Date    : 2020/9/14
# @Version : 1.0

import os
from time import time
from selenium.webdriver.chrome.webdriver import WebDriver
from common.logger import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basePath import ERROR_IMG_DIR


class BasePage:
    """页面基础操作封装"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def screen_shot(self, img_info):
        """
        屏幕截图
        :param img_info:截图保存信息
        :return:
        """
        current_time = time()
        filename = '{}_{}.png'.format(img_info, current_time)
        filepath = os.path.join(ERROR_IMG_DIR, filename)
        self.driver.save_screenshot(filepath)
        log.info("错误页面已保存，路径为：{}".format(filepath))

    def get_element(self, loc, img_info):
        """
        封装find_element
        :param loc:
        :param img_info:
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            log.error("定位{}元素失败".format(loc))
            log.exception(e)
            self.screen_shot(img_info)
        else:
            log.info("定位{}元素成功".format(loc))
            return ele

    def wait_element_visible(self, loc, img_info, timeout=15, poll_frequency=0.5):
        """
        等待元素可见
        :param loc:定位元素表达式
        :param img_info:发生错误时截图文件名
        :param timeout:等待超时时间
        :param poll_frequency:查询频率
        :return:超时错误或者元素
        """
        # 获取当前时间
        start_time = time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            # 输出错误日志
            log.error("元素{}等待可访问超时".format(loc))
            log.exception(e)
            # 对当前错误页面截图
            self.screen_shot(img_info)
            raise e
        else:
            # 打印等待时间，返回元素
            end_time = time()
            log.info('元素{}可访问，等待时间{}秒'.format(loc, start_time - end_time))
            return ele

    def wait_element_clickable(self, loc, img_info, timeout=15, poll_frequency=0.5):
        """
        等待元素可点击
        :param loc:定位元素表达式
        :param img_info:发生错误时截图文件名
        :param timeout:等待超时时间
        :param poll_frequency:查询频率
        :return:超时错误或者元素
        """
        # 获取当前时间
        start_time = time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            # 输出错误日志
            log.error("元素{}等待可点击超时".format(loc))
            log.exception(e)
            # 对当前错误页面截图
            self.screen_shot(img_info)
            raise e
        else:
            # 打印等待时间，返回元素
            end_time = time()
            log.info('元素{}可点击，等待时间{}秒'.format(loc, start_time - end_time))
            return ele

    def wait_element_present(self, loc, img_info, timeout=15, poll_frequency=0.5):
        """
        等待元素出现
        :param loc:定位元素表达式
        :param img_info:发生错误时截图文件名
        :param timeout:等待超时时间
        :param poll_frequency:查询频率
        :return:超时错误或者元素
        """
        # 获取当前时间
        start_time = time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except Exception as e:
            # 输出错误日志
            log.error("元素{}等待出现超时".format(loc))
            log.exception(e)
            # 对当前错误页面截图
            self.screen_shot(img_info)
            raise e
        else:
            # 打印等待时间，返回元素
            end_time = time()
            log.info('元素{}可点击，等待时间{}秒'.format(loc, start_time - end_time))
            return ele

    def get_element_text(self, loc, img_info):
        """
        获取元素文本信息
        :param loc:定位器
        :param img_info:错误截图信息
        :return:text
        """
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            log.error("获取{}元素文本失败".format(loc))
            log.exception(e)
            self.screen_shot(img_info)
            raise e
        else:
            log.info("获取{}元素文本成功".format(loc))
            return text

    def get_element_attr(self, loc, attr_name, img_info):
        """
        获取元素属性
        :param loc:定位器
        :param attr_name:属性名称
        :param img_info:错误截图信息
        :return:
        """
        try:
            attr_value = self.driver.find_element(*loc).get_attribute(attr_name)
        except Exception as e:
            log.error("获取{}元素属性失败".format(loc))
            log.exception(e)
            self.screen_shot(img_info)
            raise e
        else:
            log.info("获取{}元素属性成功".format(loc))
            return attr_value

    def click_element(self, loc, img_info):
        """
        click封装
        :param loc:
        :param img_info:
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            log.error("元素{}点击失败".format(loc))
            log.exception(e)
            self.screen_shot(img_info)
            raise e
        else:
            log.info("元素{}点击成功".format(loc))

    def input_text(self, loc, text, img_info):
        """
        文本输入
        :param loc:
        :param text:文本内容
        :param img_info:
        :return:
        """
        try:
            self.driver.find_element(*loc).send_keys(text)
        except Exception as e:
            log.error("文本{}输入失败".format(text))
            log.exception(e)
            self.screen_shot(img_info)
            raise e
        else:
            log.info("文本{}输入成功".format(text))

