# -*- coding:utf-8 -*-
# /usr/bin/env python
# @Author: yangzhao
# @Time: 2021-01-12
# @IDE :Pycharm
# @File: cpu_status.py
import os

CHROME_PACKAGE = 'com.mobvoi.ticauto.player'  # 'com.android.browser'


class cpu_status(object):
    def __init__(self):
        self.res_info = ""


    """ 获取CPU占有率"""
    def get_top_cpu(self):
        """
        -m num  Maximum number of processes to display. 最多显示所多少进程
        -n num  Updates to show before exiting. 刷新频率
        -d num  Seconds to wait between updates. 间隔时间
        -s col  Column to sort by (cpu,vss,rss,thr). 排序方式
        """
        cmd = "adb shell top -m 100 -d 5 -n 1 | grep {}".format(CHROME_PACKAGE)
        self.res_info = os.popen(cmd)

        """ top命令返回格式: PID PR CPU% S  #THR     VSS     RSS PCY UID      Name """

    def get_cpu_value(self):
        for value in self.res_info.readlines():





class Controll(object):
    def __init__(self, count):
        self.count = count

    def run(self):
        while self.count > 0:


