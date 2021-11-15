# coding: utf-8
#
# import uiautomator2 as u2
import time

from .base import base as d

# d = u2.connect('127.0.0.1:7555')

# 1280 720
# d(text="浏览器").click()
# 高度、宽度
h = 1280
w = 720

# 进入副本
d.click(0.89 * h, 0.464 * w)
time.sleep(2)

# 找到交易市场
d.swipe(0.904 * h, 0.46 * w, 0.162 * h, 0.464 * w)
time.sleep(2)
d.swipe(0.904 * h, 0.46 * w, 0.162 * h, 0.464 * w)
time.sleep(2)
d.swipe(0.904 * h, 0.46 * w, 0.162 * h, 0.464 * w)
time.sleep(2)

# 进入交易市场
d.click(0.808 * h, 0.801 * w)
time.sleep(2)
# 收菜
d.click(0.9 * h, 0.925 * w)
time.sleep(2)
d.click(0.51 * h, 0.78 * w)
time.sleep(2)
d.click(0.04 * h, 0.031 * w)
time.sleep(2)
d.click(0.596 * h, 0.68 * w)
time.sleep(2)

# 进入交易市场
d.click(0.808 * h, 0.801 * w)
time.sleep(2)
# 收菜
d.click(0.9 * h, 0.925 * w)
time.sleep(2)
d.click(0.51 * h, 0.78 * w)
time.sleep(2)
d.click(0.04 * h, 0.031 * w)
time.sleep(2)
d.click(0.596 * h, 0.68 * w)
time.sleep(2)

# 退出 回到首页
d.click(0.044 * h, 0.039 * w)
time.sleep(2)
