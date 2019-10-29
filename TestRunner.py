from lib.MyLogger import createLogger
import sys
import os
import logging

class TestRunner():
    def __init__(self):
        pass

if __name__ == '__main__':
    runner = TestRunner()
    logger = createLogger()
    rootlogger = logger[0]
    rootloggerpath = logger[1]
    rootlogger.info("test root logger")

    logger = createLogger(name = "mylogger", path = rootloggerpath + '\\')
    mylogger = logger[0]
    myloggerpath = logger[1]
    mylogger.info("test my logger")

    mylogger.info("test only my logger1")

    mylogger.info("test only my logger2")