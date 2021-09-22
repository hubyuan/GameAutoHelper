# coding: utf-8
#
# import uiautomator2 as u2
import time

import check as ch
from base import base as d


def doing():
    d = d()
    h = 1280
    w = 720

    # 进入副本
    d.click(0.89, 0.464)
    time.sleep(2)

    # 找到勇者
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)
    while (ch.checkyz() < 10.0):
        operation()

    # 退出 回到首页
    d.click(0.816, 0.106)
    time.sleep(2)


def operation():
    # 进入交易市场
    d.click(0.558, 0.783)
    time.sleep(2)
    # 收菜
    d.click(0.472, 0.804)
    time.sleep(2)
    d.click(0.502, 0.719)
    time.sleep(2)
    d.click(0.81, 0.099)
    time.sleep(2)


if __name__ == '__main__':
    doing()
