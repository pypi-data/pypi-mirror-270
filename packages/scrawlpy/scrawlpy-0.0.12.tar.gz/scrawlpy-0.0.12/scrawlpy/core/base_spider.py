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

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.spider_config = None
        self.logger = get_bind_logger(self.spider_name)
        self.requests = None
        self.is_daemon = False
        self.requests: Request = Request()

        if self.__custom_setting__:
            for key, value in self.__custom_setting__.items():
                setattr(Settings, key, value)
        if kwargs.get("settings") and isinstance(kwargs["settings"], dict):
            cmd_settings: dict = kwargs["settings"]
            for key, value in cmd_settings.items():
                setattr(Settings, key, value)

        self.logger.debug(Settings())

    # def start_requests(self):
    #     pass

    def parse(self, response, **kwargs):
        pass
