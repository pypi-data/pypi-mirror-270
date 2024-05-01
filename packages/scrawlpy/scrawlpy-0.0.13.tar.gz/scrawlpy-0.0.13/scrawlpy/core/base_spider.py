# -*- coding: utf-8 -*-
# @Time   : 2024/4/28 16:29
import copy
import json
import time
import traceback
import uuid
from abc import ABCMeta, abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from typing import Iterable, Union

import requests
from urllib3.exceptions import InsecureRequestWarning

from scrawlpy.http.request import Request
from scrawlpy.utils.logger_util import get_bind_logger
from scrawlpy.setting import Settings

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class AbstractSpider(metaclass=ABCMeta):
    project_name = "abstract_project"  # 项目
    spider_name = "abstract_spider"  # spider 接口
    site = "abstract"  # 站点
    Request = Request
    __custom_setting__ = dict()
    Settings = Settings

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.spider_config = None
        self.logger = get_bind_logger(self.spider_name)
        self.requests = None
        self.is_daemon = False
        self.requests: Request = Request()
        self.settings: Settings = self.get_settings(kwargs.get("settings"))
        self.settings_extra = self.settings.Extra

        self.logger.debug(json.dumps(self.settings.__dict__, indent=4))

    def get_settings(self, cmd_settings) -> Settings:
        """
        获取设置
        Args:
            cmd_settings:

        Returns:

        """

        if not cmd_settings:
            cmd_settings = dict()
        # 合并自定义设置和命令行设置，命令行设置优先级更高
        combined_settings = {**self.__custom_setting__, **cmd_settings}
        # 过滤掉Settings类中不存在的字段
        valid_settings = {key: value for key, value in combined_settings.items()
                          if key in self.Settings.get_field_list()}

        # 提取Settings类中不存在的额外设置, 因为 attr 里，如果未定义的变量传入会报错
        extra_settings = {key: value for key, value in combined_settings.items()
                          if key not in valid_settings}

        # 将有效的设置和额外设置传递给Settings类的构造函数
        settings = self.Settings(
            **valid_settings,
            Extra=extra_settings if extra_settings else None
        )
        return settings

    # def start_requests(self):
    #     pass

    def parse(self, response, **kwargs):
        pass
