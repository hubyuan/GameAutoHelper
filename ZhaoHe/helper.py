# coding: utf-8
import os

from ZhaoHe.click_location import *


class helper:
    isconnet = 0

    def __init__(self):
        if (helper.isconnet == 0):
            os.system(BASE['connect'])
            helper.isconnet += 1

    # 手动连接
    def connet(self):
        os.system(BASE['connect'])

    # 点击
    def click(self, x, y):
        text = 'input tap ' + str(x * BASE['h']) + ' ' + str(y * BASE['w'])
        os.system(BASE['suffix'] + text)

    # 滑动
    def swipe(self, x1, y1, x2, y2):
        text = 'input swipe {} {} {} {} '.format(str(int(x1 * BASE['h'])), str(int(y1 * BASE['w'])),
                                                 str(int(x2 * BASE['h'])), str(int(y2 * BASE['w'])))
        os.system(BASE['suffix'] + text)

    # 滑动
    def swipe1(self, x1, y1, x2, y2):
        text = 'input swipe {} {} {} {} '.format(str(int(x1)), str(int(y1)),
                                                 str(int(x2 * BASE['h'])), str(int(y2 * BASE['w'])))
        os.system(BASE['suffix'] + text)

    # 滑动
    def swipeXY(self, XY):
        text = 'input swipe {} {} {} {} '.format(str(int(XY[0][0] * BASE['h'])), str(int(XY[0][1] * BASE['w'])),
                                                 str(int(XY[1][0] * BASE['h'])), str(int(XY[1][1] * BASE['w'])))
        os.system(BASE['suffix'] + text)

    # 截屏
    def screencap(self):
        os.system(BASE['suffix'] + 'screencap  -p ' + BASE['img_name'])
        os.system(BASE['suffixsimple'] + 'pull ' + BASE['img_name'] + ' ' + BASE['path_tmp'])


if __name__ == '__main__':
    print()
