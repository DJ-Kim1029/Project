#-*- coding:utf-8 -*-
import logging
import time
import os


FORMATTER = logging.Formatter('%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')

def logTime():
    ret_time = time.strftime('%y%m%d_%H%M%S', time.localtime(time.time()))
    return ret_time

def createLogger(name = None, level=logging.INFO, path='.\log'):
    if name == None :
        logger_name = logTime() + '_' + "TestRunner"
        # create logger
        create_logger = logging.getLogger()
    else :
        logger_name = logTime() + '_' + name
        # create logger
        create_logger = logging.getLogger(logger_name)

    logger_folder = path + '\\' + logger_name

    create_logger.setLevel(level)

    if name == None :
        # create stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(FORMATTER)
        create_logger.addHandler(stream_handler)

    # create file handler
    try:
        if not os.path.exists(logger_folder):
            os.mkdir(logger_folder)
    except OSError:
        pass

    file_handler = logging.FileHandler(logger_folder + '\\' + logger_name + '.log')
    file_handler.setFormatter(FORMATTER)
    create_logger.addHandler(file_handler)

    return create_logger, logger_folder

if __name__ == '__main__':
    logger = createLogger(path = '..\log')
    rootlogger = logger[0]
    rootloggerpath = logger[1]
    rootlogger.info('test root logger')


    logger = createLogger(name = 'mylogger', path = rootloggerpath + '\\')
    mylogger = logger[0]
    myloggerpath = logger[1]
    mylogger.info('test my logger')