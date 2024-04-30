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
from scrawlpy.http.request import Request


class AbstractSpider(metaclass=ABCMeta):
    project_name = ""  # 项目
    site = ""  # 站点
    spider_name = ""  # spider 接口
    Request = Request

    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.spider_config = None
        self.log = None
        self.requests = None
        self.requests: Request = Request()
