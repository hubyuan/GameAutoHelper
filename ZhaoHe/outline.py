# coding: utf-8
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from ZhaoHe.click_location import *
from ZhaoHe.screenshot import *

d = helper()
screen = screenshot()


def get_screen_XY():
    print('找框架')
    img = cv.imread(BASE['img_tmp'])
    draw = img.copy()
    gray = cv.cvtColor(draw, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    x = 0
    y = 0
    contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_new = []
    for i in contours:
        count = 0
        for j in i:
            count += 1

        if (count > 3 and count < 5 and i[0][0][0] < 1000 and
                i[0][0][0] > 200 and i[0][0][0] == i[1][0][0] and
                i[2][0][0] == i[3][0][0] and i[0][0][1] == i[3][0][1] and
                i[1][0][1] == i[2][0][1] and i[1][0][0] - i[0][0][0] + i[1][0][1] - i[0][0][1] > 20):
            x = i[0][0][0] + (i[1][0][0] - i[0][0][0]) / 2
            y = i[0][0][1] + (i[1][0][1] - i[0][0][1]) / 2
            contours_new.append(i)
    return (x, y)


if __name__ == '__main__':
    x, y = get_screen_XY()
    print(x)
    print(y)
