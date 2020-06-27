# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:13:30 2020

@author: mchsiaoj

modified from https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
"@functools.wraps(func)" recommend by "Python Tricks: A Buffet of Awesome Python Features"

"""

import functools
import time


def tictoc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            log_name = kwargs.get('log_name', func.__name__)
            kwargs['log_time'][log_name] = te - ts
        else:
            print('%s(): Elapsed time is %g seconds.'%(func.__name__, te - ts))
        return result
    return wrapper