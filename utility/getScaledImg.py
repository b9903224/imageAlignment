# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:15:55 2020

@author: b9903
"""

import numpy as np

def getScaledImg(srcImg):
    imgH, imgW, imgZ = getImgSize(srcImg)    
    if srcImg.dtype != np.uint8:
        return srcImg
    elif (imgZ != 0) and (imgZ != 3):
        return srcImg
    resultImg = np.copy(srcImg)    
    resultImg.astype(np.int16)
    if imgZ == 0:
        resultImg = getScaledImgByCh(resultImg)        
    else:
        for ch in range(imgZ):
            resultImg[:,:,ch] = getScaledImgByCh(resultImg[:,:,ch])
    
    resultImg = resultImg.astype(np.uint8)
    return resultImg

def getScaledImgByCh(resultImg):
    mn = np.min(resultImg)
    mx = np.max(resultImg)
    if mn != mx:
        resultImg = (resultImg - mn)/(mx-mn)*255
    return resultImg

def getImgSize(img):
    imgZ = 0
    imgH = img.shape[0]
    imgW = img.shape[1]
    if img.ndim == 3:
        imgZ = img.shape[2]
    return imgH, imgW, imgZ