# -*- coding: utf-8 -*-
# @Time   : 2024/4/28 16:55

import scrawlpy
from scrawlpy import Request


# from urllib3 import HTTPHeaderDict


class Myspider(scrawlpy.Spider):
    def run(self):
        res = self.requests.get("http://www.baidu.com")
        print(res.text)


if __name__ == '__main__':
    Myspider("dda").run()
