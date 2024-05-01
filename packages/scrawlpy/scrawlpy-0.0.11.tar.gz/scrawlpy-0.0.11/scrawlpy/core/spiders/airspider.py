# -*- coding: utf-8 -*-
# @Time   : 2024/4/30 17:16
import multiprocessing
import os
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from func_timeout import func_set_timeout

from scrawlpy.core.base_spider import AbstractSpider
from scrawlpy.storage.memorydb import MemoryDB
from scrawlpy.utils.concurrent_util import ThreadUtil
from scrawlpy.utils.tail_thread import TailThread
from scrawlpy.setting import Settings
# from scrawlpy.commands.spider import main
shutdown_event = multiprocessing.Event()


class AirSpider(AbstractSpider, TailThread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        self.thread_num = self.kwargs.get("thread_num", 1)
        self.crawler_threads = []
        self.request_queue = MemoryDB()
        # main()

    def start_task_distribute(self) -> None:
        """
        分发任务
        Returns:

        """
        while True:
            self.request_queue.add({"url": "https://www.baidu.com"}, 1)
            self.request_queue.add({"url": "https://www.qq.com"}, 2)

        # with ThreadPoolExecutor(max_workers=self.thread_num) as executor:
        #     executor.map(self._process_job, job_list)

    def _start_requests(self):
        # seed = self.start_requests()

        seed = self.request_queue.get_nowait()
        while seed and not shutdown_event.is_set():
            self.start_requests(seed)
            seed = self.request_queue.get_nowait()
        self.start_requests(seed)

    def start_requests(self, seed):
        print(seed)

    # def run(self):
    #
    #     ThreadUtil.bg_run_task_on_thread(self.start_task_distribute, args=())
    #     self.start_task_distribute()
    #     for i in range(self.thread_num):
    #         t = threading.Thread(target=self._start_requests)
    #         t.start()
    #         t.join()
            # self.crawler_threads.append(t)

    # @func_set_timeout(5)
    # @func_set_timeout(Settings.Timeout or os.environ.get("TIMEOUT", 10))
    def shutdown_process(self, crawler_process):
        time.sleep(Settings.Timeout)  # 在关闭之前等待3分钟
        shutdown_event.set()
        crawler_process.join()
        self.logger.info(f"{threading.get_ident()} 已到超时时间{Settings.Timeout}，关闭当前线程...")

    def run_spider(self) -> None:
        """
        启动爬虫
        Returns:

        """
        ThreadUtil.bg_run_task_on_thread(self.start_task_distribute, args=())

        # 创建定时关闭进程的线程
        for i in range(self.thread_num):
            crawler_thread = threading.Thread(target=self._start_requests)
            crawler_thread.start()

            # 创建定时关闭进程的线程
            shutdown_thread = threading.Thread(target=self.shutdown_process, args=(crawler_thread,))
            shutdown_thread.start()


if __name__ == '__main__':
    spider = AirSpider(thread_num=2)
    spider.run_spider()
    # spider.start_task_distribute()
    # spider.run
