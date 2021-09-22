# coding: utf-8
import math
import operator
from functools import reduce

import cv2 as cv
from PIL import Image

from ZhaoHe.helper import *


class screenshot:

    def cutting(self, XY, file_name, refresh):
        d = helper()
        if refresh:
            d.screencap()
        img = cv.imread(BASE['img_tmp'], 0)
        # 对图片进行切割
        dstImg = img[int(XY[0][1] * BASE['w']):int(XY[1][1] * BASE['w']),
                 int(XY[0][0] * BASE['h']):int(XY[1][0] * BASE['h'])]
        cv.imwrite(BASE['img_path'] + file_name, dstImg)

    def compare(self, XY, file_name, refresh):
        """

        @参数一: XY X,Y DX,DY
        @参数二: file_name 要对比的图片
        """
        d = helper()
        if refresh:
            d.screencap()
        img = cv.imread(BASE['img_tmp'], 0)
        # 对图片进行切割
        dstImg = img[int(XY[0][1] * BASE['w']):int(XY[1][1] * BASE['w']),
                 int(XY[0][0] * BASE['h']):int(XY[1][0] * BASE['h'])]
        cv.imwrite(BASE['img_cut'], dstImg)
        return self.compare_images(BASE['img_cut'], FILE_NAME[file_name])

    def compareAll(self, XY, file_names, refresh):
        """

        @参数一: XY X,Y DX,DY
        @参数二: file_name 要对比的图片
        """
        d = helper()
        if refresh:
            d.screencap()
        img = cv.imread(BASE['img_tmp'], 0)
        # 对图片进行切割
        dstImg = img[int(XY[0][1] * BASE['w']):int(XY[1][1] * BASE['w']),
                 int(XY[0][0] * BASE['h']):int(XY[1][0] * BASE['h'])]
        cv.imwrite(BASE['img_cut'], dstImg)
        tag_value = 100
        for name in file_names:
            value = self.compare_images(BASE['img_cut'], FILE_NAME[name])
            if (tag_value > value):
                tag_value = value

        return tag_value

    def compare_images(self, path_one, path_two):
        """
        比较图片，如果有不同则生成展示不同的图片

        @参数一: path_one: 第一张图片的路径
        @参数二: path_two: 第二张图片的路径
        """
        image_one = Image.open(path_one)
        image_two = Image.open(path_two)

        histogram1 = image_one.histogram()
        histogram2 = image_two.histogram()

        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        return differ


if __name__ == '__main__':
    s = screenshot()
