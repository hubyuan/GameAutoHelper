import math
import operator
from functools import reduce

import cv2 as cv
from PIL import Image


def compare_images(path_one, path_two):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        # diff = ImageChops.difference(image_one, image_two)
        histogram1 = image_one.histogram()
        histogram2 = image_two.histogram()

        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))

        return differ



    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))


def comparejy():
    d = d()
    d.screencap()
    img = cv.imread('..\\resource\\img\\tmp\\01.png', 0)
    ww = 1280
    hh = 720
    # 要被切割的开始的像素的高度值
    beH = 0.723 * hh
    # 要被切割的结束的像素的高度值
    hEnd = 0.804 * hh
    # 要被切割的开始的像素的宽度值
    beW = 0.776 * ww
    # 要被切割的结束的像素的宽度值
    wLen = 0.852 * ww
    # 对图片进行切割
    dstImg = img[int(beH):int(hEnd), int(beW):int(wLen)]
    cv.imwrite('../resource/img/notallow1.png', dstImg)
    return compare_images('../resource/img/notallow1.png', '../resource/img/notallow.png')


if __name__ == '__main__':
    img = cv.imread('..\\resource\\img\\tmp\\01.png', 0)

    # 725 88     1682 1035

    ww = 1280
    hh = 720

    # 00 01 10 11
    # d.click(0.776, 0.723)
    # d.click(0.852, 0.804)

    # 要被切割的开始的像素的高度值
    beH = 0.723 * hh
    # 要被切割的结束的像素的高度值
    hEnd = 0.804 * hh
    # 要被切割的开始的像素的宽度值
    beW = 0.776 * ww
    # 要被切割的结束的像素的宽度值
    wLen = 0.852 * ww
    # 对图片进行切割
    dstImg = img[int(beH):int(hEnd), int(beW):int(wLen)]
    cv.imwrite('../resource/img/notallow1.png', dstImg)
    compare_images('../resource/img/notallow1.png', '../resource/img/notallow.png')
