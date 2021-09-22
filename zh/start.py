# coding: utf-8
#
# import uiautomator2 as u2
import time

from base import base as d


def doing():
    h = 1280
    w = 720

    # 进入游戏
    d.click(0.328, 0.375)

    # 进入界面
    d.click(0.84, 0.074)

    d.click(0.84, 0.074)

    # 领取砖石
    d.click(0.502, 0.719)

    # 领取宝蛋
    d.click(0.05, 0.893)
    # 跳过
    d.click(0.904, 0.936)


# 确认
d.click(0.498, 0.776)


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
