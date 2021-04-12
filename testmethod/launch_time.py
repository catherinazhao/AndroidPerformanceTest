# -*- coding:utf-8 -*-
# /usr/bin/env python
# @Author: yangzhao
# @Time: 2021-01-11
# @IDE :Pycharm
# @File: launch_time.py
import csv
import os
import time
import unittest


CHROME_PACKAGE = 'com.mobvoi.ticauto.player'  # 'com.android.browser'
CHROME_ACTIVITY = 'com.mobvoi.ticauto.player.ui.ContentActivity'  # 'com.android.browser.BrowserActivity'


class App(object):
    def __init__(self):
        self.content = ""
    # def setUp(self) -> None:

    # def tearDown(self) -> None:

    """ 启动APP """
    def launch_app(self):
        cmd = 'adb shell am start -W -n %s/%s' % (CHROME_PACKAGE, CHROME_ACTIVITY)
        self.content = os.popen(cmd)

    """ 热启动关闭APP (发送时间3, 表示点击Home键)"""
    def hot_stop_app(self):
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    """ 冷启动关闭App """
    def cold_stop_app(self):
        cmd = 'adb shell am force-stop %s' % CHROME_PACKAGE
        os.popen(cmd)

    """ 取得启动时间 """
    def get_launch_time(self):
        for line in self.content.readlines():
            print(line)
            if "ThisTime" in line:
                elpased_time = line.split(":")[-1]
                break

        return elpased_time


class Control(object):
    def __init__(self, count):
        self.counter = count
        self.app = App()
        self.all_data = [("TimeStamp", "LaunchTime")]

    def run(self):
        self.app.cold_stop_app()
        while self.counter > 0:
            print(11111111111, self.counter)
            time.sleep(1)
            self.app.launch_app()
            elpased_time = self.app.get_launch_time()
            time.sleep(1)
            time_stamp = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            # self.app.cold_stop_app()
            self.app.hot_stop_app()
            self.counter = self.counter - 1
            self.all_data.append((time_stamp, elpased_time))

    """ 存储数据到csv文件中 """
    def save_data_to_xls(self):
        with open("result.csv", "w+") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    ctl = Control(10)
    ctl.run()
    ctl.save_data_to_xls()