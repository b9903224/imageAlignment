# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:06:27 2019

@author: b9903

set operation:
    if input_list == [True, 1, 1] --> (True)
    if input_list == [1, True, 1] --> (1)

"""

def printUniqueRatio(input_list):
#    input_list_unique = []
#    for value in input_list:
#        if value not in input_list_unique:
#            input_list_unique.append(value)
    input_list_unique = set(input_list)
    
    list_len = len(input_list)
    for index, value in enumerate(input_list_unique):
        count = input_list.count(value)
        ratio = count / list_len
        print('index: {} - {}: {:.2%}({}/{})'.\
              format(index, value, ratio, count, list_len))