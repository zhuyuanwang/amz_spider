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

class MainSpider(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        pass
