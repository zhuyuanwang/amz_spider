# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 23:29
# @Author  : Circleone_

import json
import re
import sys
import time
import redis
import requests
import traceback
import threading
from multiprocessing import Queue, Process
THREAD_NUM = 4
PROCESS_NUM = 8

class MainSpider(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        pass

def start_spider(y, task_set):
    threads = []
    for i in range(THREAD_NUM):
        num = str(y) + '-' + str(i + 1)
        t = MainSpider(num, task_set)
        t.start()
        threads.append(t)

def thread_start_review(task_set):
    p_list = []
    for y in range(PROCESS_NUM):
        p = Process(target=start_spider, args=(y,task_set))
        p.start()
        p_list.append(p)
        time.sleep(1)
    for p in p_list:
        p.join()

if __name__ == '__main__':
    pass
