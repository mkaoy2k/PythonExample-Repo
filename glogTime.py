"""Measuring an elapsed time of function execution
by creating a timestamp object, inAndOutLog, using 'glog' module.
用法:

@func_timer_decorator
def xyz():
    ...

當 xyz() 函式執行後，會看見 'func_timer_decorator' 執行後的結果，
套用在 xyz() 函式上。
"""
import glog as log
import datetime


class inAndOutLog():
    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        log.info(f'開始: {self.funcName}')
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        log.info(
            f'結束: {self.funcName} 共花 {datetime.datetime.now() - self.init_time} 秒.\n')


def func_timer_decorator(func):

    def func_wrapper(*args, **kwargs):
        with inAndOutLog(func.__name__):
            return func(*args, **kwargs)
    return func_wrapper
