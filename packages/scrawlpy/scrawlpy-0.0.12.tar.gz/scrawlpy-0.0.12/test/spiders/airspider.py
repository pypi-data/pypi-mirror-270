# -*- coding: utf-8 -*-
# @Time   : 2024/4/28 16:55

import scrawlpy
from scrawlpy import Request


# from urllib3 import HTTPHeaderDict

class Myspider(scrawlpy.AirSpider):
    __custom_setting__ = {
        "Timeout": 5,
        # "KEEP_ALIVE": False,
    }

    def start_requests(self, seed):
        # print(seed)
        priority, seed = seed
        # self.log.info()
        url = seed.get("url")
        res = self.requests.get(url)
        self.logger.info(res.text)
        # for i in range(10):
        #     yield Request("http://www.baidu.com", callback=self.parse)
        # res = self.requests.get("http://www.baidu.com")
        # print(res.text)


if __name__ == '__main__':
    Myspider(thread_num=1).start()
