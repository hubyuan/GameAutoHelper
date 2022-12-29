# coding: utf-8
# !/usr/bin/python3
import ctypes
import inspect

from ZhaoHe.helper import helper
from daka.gamecopy import *

import threading


class myThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        plan()


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread()

    # 开启线程
    thread1.start()

    thread1.join(timeout=60 * 30)

    if thread1.is_alive():
        stop_thread(thread1)
