# coding: utf-8
#
# import uiautomator2 as u2
import time

from base import base as d

if __name__ == '__main__':
    # d = u2.connect('127.0.0.1:7555')

    # 1280 720
    # d(text="浏览器").click()
    h = 1280
    w = 720

    # 进入副本
    d.click(0.89, 0.464)
    time.sleep(2)

    # 找到交易市场
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)
    d.swipe(0.904, 0.46, 0.162, 0.464)
    time.sleep(2)

    # 进入交易市场
    d.click(0.808, 0.801)
    time.sleep(2)
    # 收菜
    d.click(0.9, 0.925)
    time.sleep(2)
    d.click(0.51, 0.78)
    time.sleep(2)
    d.click(0.04, 0.031)
    time.sleep(2)
    d.click(0.596, 0.68)
    time.sleep(2)

    # 进入交易市场
    d.click(0.808, 0.801)
    time.sleep(2)
    # 收菜
    d.click(0.9, 0.925)
    time.sleep(2)
    d.click(0.51, 0.78)
    time.sleep(2)
    d.click(0.04, 0.031)
    time.sleep(2)
    d.click(0.596, 0.68)
    time.sleep(2)

    # 退出 回到首页
    d.click(0.044, 0.039)
    time.sleep(2)
