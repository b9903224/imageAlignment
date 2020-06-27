# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:54:39 2020

@author: b9903
"""

def getImgSize(img):
    imgZ = 0
    imgH = img.shape[0]
    imgW = img.shape[1]
    if img.ndim == 3:
        imgZ = img.shape[2]
    return imgH, imgW, imgZ