# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:57:22 2020

@author: b9903
"""

import functools
import traceback


def exception_dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        errMsg = ''
        try:
            result = func(*args, **kwargs)
        except:
            errMsg = traceback.format_exc()
        return {'result': result, 'errMsg': errMsg}
    return wrapper