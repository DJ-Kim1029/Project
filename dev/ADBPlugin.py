#-*- coding:utf-8 -*-
from subprocess import *

if __name__ == '__main__':
    call(["adb", "shell", "input", "tap", "874", "2150"], shell = True)