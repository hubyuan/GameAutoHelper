import os

h = 1280
w = 720
# 进入副本


suffix = 'D:\\soft\\SOFT\\adb\\adb -s 127.0.0.1:7555 shell '
suffixsimple = 'D:\\soft\\SOFT\\adb\\adb -s 127.0.0.1:7555 '
img_src = '../resource/img/tmp'
img_name = '/sdcard/01.png'


class base:
    isconnet = 0

    def __init__(self):
        if (self.isconnet == 0):
            os.system('D:\\soft\\SOFT\\adb\\adb connect 127.0.0.1:7555')
            self.isconnet = 1

    def click(self, x, y):
        text = 'input tap ' + str(x * h) + ' ' + str(y * w)
        # text = 'input tap ' + str(0.89 * h) + ' ' + str(0.464 * w)
        os.system(suffix + text)

    def swipe(self, x1, y1, x2, y2):
        text = 'input swipe {} {} {} {} '.format(str(int(x1 * h)), str(int(y1 * w)), str(int(x2 * h)), str(int(y2 * w)))
        # command = "input swipe {} {} {} {} ".format(x1, y1, x2, y2)
        # text = 'input tap ' + str(0.89 * h) + ' ' + str(0.464 * w)
        os.system(suffix + text)

    def screencap(self):
        os.system(suffix + 'screencap  -p ' + img_name)
        os.system(suffixsimple + 'pull ' + img_name + ' ' + img_src)


if __name__ == '__main__':
    print()
