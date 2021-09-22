# coding: utf-8
#
import logging
import time
import _thread
import datetime
from ZhaoHe.click_location import *
from ZhaoHe.screenshot import *
from ZhaoHe import outline

d = helper()
# line = outline()
screen = screenshot()
logger = logging.getLogger('gamecopy')
logger.setLevel(logging.INFO)
logging.FileHandler('D:/code/GameAutoHelper/log/zhaohe.log')


def jiaoyi():
    """
        副本交易市场
    """
    back()
    # 进入副本
    d.click(CLICK_LOCATION['COPY'][0], CLICK_LOCATION['COPY'][1])
    time.sleep(2)

    # 找到交易市场
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    while (screen.compare(MAP_LOCATION['JIAOYI'], 'JIAOYI', 1) < 10.0):
        operation_jy()


def operation_jy():
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


def yongzhe():
    """
        副本勇者
    """
    back()
    # 进入副本
    d.click(CLICK_LOCATION['COPY'][0], CLICK_LOCATION['COPY'][1])
    time.sleep(2)

    # 找到勇者
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    while (screen.compare(MAP_LOCATION['YONGZHE'], 'YONGZHE', 1) < 10.0):
        operation_yz()

    # 退出 回到首页
    d.click(0.816, 0.106)
    time.sleep(2)


def operation_yz():
    # 进入勇者
    d.click(0.558, 0.783)
    time.sleep(2)
    # 收菜
    d.click(0.472, 0.804)
    time.sleep(2)
    d.click(0.502, 0.719)
    time.sleep(2)
    d.click(0.81, 0.099)
    time.sleep(2)


def jiayuan():
    back()
    # 进入副本
    d.click(CLICK_LOCATION['HOME'][0], CLICK_LOCATION['HOME'][1])
    time.sleep(5)
    opration_jia()


def opration_jia():
    d.swipeXY(MAP_LOCATION['SLIDE'])
    time.sleep(2)
    d.click(0.756, 0.379)
    time.sleep(2)
    d.click(0.502, 0.854)
    time.sleep(2)
    d.click(0.594, 0.68)
    time.sleep(2)
    d.click(0.504, 0.776)


def cangbaotu():
    # 藏宝图
    back()
    # 进入任务
    d.click(CLICK_LOCATION['TASK'][0], CLICK_LOCATION['TASK'][1])
    time.sleep(2)
    operation_cbt()


def operation_cbt():
    # 碎片获取
    d.click(0.364, 0.127)
    time.sleep(2)
    if (screen.compare(MAP_LOCATION['TREASURE_MAP'], 'TREASURE_MAP', 1) < 2.0):
        return
    # 加体力
    d.click(0.622, 0.042)
    time.sleep(2)
    d.click(0.588, 0.677)
    time.sleep(2)
    # 加体力
    # d.click(0.622, 0.042)
    # time.sleep(2)
    # d.click(0.588, 0.677)
    # time.sleep(2)

    d.click(0.504, 0.822)
    time.sleep(3)
    d.click(0.498, 0.776)
    time.sleep(3)


def opration_ycy():
    # start

    d.click(0.504, 0.907)
    time.sleep(3)
    d.click(0.568, 0.812)
    time.sleep(4)
    d.swipe(0.53, 0.918, 0.8, 0.918)
    time.sleep(30)
    d.click(0.496, 0.719)
    time.sleep(3)
    d.click(0.496, 0.719)
    time.sleep(3)
    d.click(0.08, 0.897)
    time.sleep(3)
    d.click(0.524, 0.879)
    time.sleep(3)
    d.click(0.592, 0.677)
    time.sleep(3)
    yiciyuan()


# 异次元

def yiciyuan():
    back()
    d.click(CLICK_LOCATION['COPY'][0], CLICK_LOCATION['COPY'][1])
    time.sleep(2)
    for i in range(5):
        d.swipe(0.402, 0.476, 0.15, 0.476)
        time.sleep(2)

    d.click(0.154, 0.783)
    time.sleep(2)

    if (screen.compare(MAP_LOCATION['YICIYUAN'], 'YICIYUAN', 1) < 10.0):
        opration_ycy()


def baodan():
    """
        领取宝蛋
    """
    back()
    while (screen.compare(MAP_LOCATION['BAODAN'], 'BAODAN', 1) < 10.0):
        d.click(CLICK_LOCATION['BAODAN'][0], CLICK_LOCATION['BAODAN'][1])
        time.sleep(2)
        d.click(CLICK_LOCATION['SKIP'][0], CLICK_LOCATION['SKIP'][1])
        time.sleep(2)
        d.click(CLICK_LOCATION['OK'][0], CLICK_LOCATION['OK'][1])
        time.sleep(2)
        logger.info('领取宝蛋成功')


# 熔炼
def ronglian():
    back()
    d.click(0.282, 0.925)
    time.sleep(2)
    d.click(0.032, 0.932)
    time.sleep(2)
    d.click(0.44, 0.567)
    time.sleep(2)

    for i in range(13):
        d.swipeXY(MAP_LOCATION['SSLIDE'])
        time.sleep(1)

    if (screen.compare(MAP_LOCATION['CHICKEN'], 'CHICKEN', 1) < 10.0):
        d.click(0.304, 0.879)
        time.sleep(3)
        d.click(0.66, 0.783)
        time.sleep(3)
        d.click(0.594, 0.673)
        time.sleep(3)
        d.click(0.496, 0.716)
        time.sleep(3)


def opration_shop():
    list = []
    refresh = 1
    for i in range(9):
        j = i + 1

        if (screen.compare(MAP_LOCATION['SHOP' + str(j)], 'WOOD', refresh) > 10.0 and screen.compare(
                MAP_LOCATION['SHOP' + str(j)], 'STONE', refresh) > 10.0):
            list.append(j)
        refresh = 0

    for i in list:
        d.click(CLICK_LOCATION['S' + str(i)][0], CLICK_LOCATION['S' + str(i)][1])
        time.sleep(1)

    if (screen.compare(MAP_LOCATION['SELL_OUT'], 'SELL_OUT', 1) > 10.0):
        # 购买
        d.click(0.656, 0.773)
        time.sleep(2)
        d.click(0.592, 0.666)
        time.sleep(2)
        d.click(0.504, 0.773)
        time.sleep(2)

    if (screen.compare(MAP_LOCATION['MASONRY'], 'MASONRY', 0) > 10.0):
        d.click(0.87, 0.819)
        time.sleep(2)
        # d.click(CLICK_LOCATION['IS_OK'][0], CLICK_LOCATION['IS_OK'][1])
        # time.sleep(2)
        opration_shop()


def opration_dk():
    # d.click(0.408, 0.78)
    # time.sleep(3)
    d.click(0.668, 0.815)
    time.sleep(3)
    d.click(0.338, 0.819)
    time.sleep(20)
    d.click(0.338, 0.819)
    time.sleep(5)


def duokuan():
    back()
    # 进入副本
    d.click(CLICK_LOCATION['COPY'][0], CLICK_LOCATION['COPY'][1])
    time.sleep(3)

    d.click(0.408, 0.78)
    time.sleep(3)
    d.click(0.51, 0.822)
    time.sleep(2)
    d.click(0.51, 0.822)
    time.sleep(4)

    if (screen.compare(MAP_LOCATION['FIGHT'], 'FIGHT', 1) > 2.0):
        print(screen.compare(MAP_LOCATION['FIGHT'], 'FIGHT', 0))
        return
    print(screen.compare(MAP_LOCATION['FIGHT'], 'FIGHT', 0))
    opration_dk()
    opration_dk()
    opration_dk()


def start_back():
    refresh = 1
    file_names = ['BACK', 'BACK1', 'BACK2', 'BACK3', 'BACK4', 'BACK5']
    if (screen.compareAll(MAP_LOCATION['BACK'], file_names, refresh) < 10.0):
        d.click(CLICK_LOCATION['BACK'][0], CLICK_LOCATION['BACK'][1])
        time.sleep(3)
        back()
    refresh = 0
    if (screen.compare(MAP_LOCATION['SOK'], 'SOK', refresh) < 10.0):
        d.click(CLICK_LOCATION['SOK'][0], CLICK_LOCATION['SOK'][1])
        time.sleep(2)
        back()
    if (screen.compare(MAP_LOCATION['OK'], 'OK', refresh) < 10.0):
        d.click(CLICK_LOCATION['OK'][0], CLICK_LOCATION['OK'][1])
        time.sleep(2)
        back()

    if (screen.compare(MAP_LOCATION['RSLIDE'], 'RSLIDE', refresh) < 10.0):
        d.click(CLICK_LOCATION['RSLIDE'][0], CLICK_LOCATION['RSLIDE'][1])
        time.sleep(2)
        back()
    if (screen.compare(MAP_LOCATION['IS_OK'], 'IS_OK', refresh) < 10.0):
        d.click(CLICK_LOCATION['IS_OK'][0], CLICK_LOCATION['IS_OK'][1])
        time.sleep(2)
        back()
    if (screen.compare(MAP_LOCATION['UP'], 'UP', refresh) < 10.0):
        d.click(CLICK_LOCATION['UP'][0], CLICK_LOCATION['UP'][1])
        time.sleep(2)
        back()


# 家园市场
def shichang():
    back()
    d.click(CLICK_LOCATION['SHOP'][0], CLICK_LOCATION['SHOP'][1])
    time.sleep(2)
    d.click(0.086, 0.812)
    time.sleep(2)

    opration_shop()


def back():
    """
        回到首页
    """
    # print(screen.compare(MAP_LOCATION['BACK'], 'BACK'))
    start_back()


def startComp(x, y, x1, y1):
    # 开始拉扯 ,拉5次
    d.swipe1(x, y, x1, y1)
    time.sleep(1)
    d.swipe1(x, y, x1, y1)
    time.sleep(1)
    d.swipe1(x, y, x1, y1)
    time.sleep(1)
    d.swipe1(x, y, x1, y1)
    time.sleep(1)
    d.swipe1(x, y, x1, y1)
    time.sleep(1)


def arena():
    back()
    d.click(CLICK_LOCATION['ARENA'][0], CLICK_LOCATION['ARENA'][1])
    time.sleep(2)

    if (screen.compare(MAP_LOCATION['START_COMPA'], 'START_COMPA', 1) < 10.0):
        # 开始匹配
        d.click(0.498, 0.904)
        time.sleep(2)
        if (screen.compare(MAP_LOCATION['START_COMPA'], 'START_COMPA', 1) < 10.0):
            # 匹配失败
            print('匹配失败,重新匹配')
            arena()

        while (screen.compare(MAP_LOCATION['WAIT_COMPA'], 'WAIT_COMPA', 1) < 10.0):
            # 匹配中
            print('匹配中')
            time.sleep(3)
        doing = 1
        x = 0
        y = 0
        x1 = 0.934
        y1 = 0.468
        all_count = 0
        while (doing):
            all_count += 1
            flag = 1
            time.sleep(1)
            if (screen.compare(MAP_LOCATION['FIGHT_COMPA'], 'FIGHT_COMPA', flag) < 10.0):
                print()
                # 停止拉扯5s
                time.sleep(5)
                all_count = 0
            flag = 0
            if (screen.compare(MAP_LOCATION['FAIL_COMPA'], 'FAIL_COMPA', flag) < 10.0 or screen.compare(
                    MAP_LOCATION['END_COMPA'], 'END_COMPA', flag) < 10.0):
                print()
                # 结束拉扯
                break
            if (screen.compare(MAP_LOCATION['DO_COMPA'], 'DO_COMPA', flag) < 10.0 or all_count > 0):

                if (x == 0 and y == 0):
                    x, y = outline.get_screen_XY()
                    if (x == 0 and y == 0):
                        continue
                # 开始拉扯
                startComp(x, y, x1, y1)
                print('开始拉扯')
                all_count = 0

            if (all_count > 3):
                print('未知错误')
                break

        d.click(0.502, 0.812)
        time.sleep(4)
        print('sssssssssssssssssssss')


def start_plan():
    print('star==================')
    baodan()
    cangbaotu()
    jiayuan()
    jiaoyi()
    yongzhe()
    duokuan()
    ronglian()
    yiciyuan()
    yiciyuan()
    shichang()
    now_time = datetime.datetime.now()
    str = datetime.datetime.strftime(now_time, '%H')
    if (int(str) < 18 and int(str) > 10):
        arena()
        arena()
    print('end==================')




def plan():
    start_plan()


def test1():
    back()
    # 进入副本
    d.click(CLICK_LOCATION['COPY'][0], CLICK_LOCATION['COPY'][1])
    time.sleep(2)
    for i in range(4):
        d.swipe(0.402, 0.476, 0.15, 0.476)
        time.sleep(2)



if __name__ == '__main__':
    arena()

    # time.sleep(2)
    # back()

    # screen.cutting(MAP_LOCATION['RSLIDE'], 'rslide.png',1)
    # screen.cutting(MAP_LOCATION['END_COMPA'], 'end_compa.png',1)

    # screen.cutting(MAP_LOCATION['DO_COMPA'], 'do_compa.png', 1)
    # screen.cutting(MAP_LOCATION['FIGHT_COMPA'], 'fight_compa.png',1)
    # print(screen.compare(MAP_LOCATION['IS_OK'], 'IS_OK'))
    # d.click(CLICK_LOCATION['SOK'][0],CLICK_LOCATION['SOK'][1])
