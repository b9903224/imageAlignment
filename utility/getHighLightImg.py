# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:15:50 2020

@author: b9903

** numpy not like Matlab if (uint8 + value) > 255 will overlow!

"""

import numpy as np

def getHighLightImg(destImg, sourceImg, rgb=[255, 0, 0], isTransparent=False, rgbBackground=[]):
#    destImg_inv = ~destImg
    destImg_inv = np.invert(destImg)
    resultImg = np.copy(sourceImg)
    if resultImg.dtype == np.bool:
        resultImg = resultImg.astype(np.uint8)*255
    imgH, imgW, imgZ = getImgSize(resultImg)
    
    if imgZ == 0:
        resultImg = np.dstack((resultImg, resultImg, resultImg))
        
    
    resultImg = resultImg.astype(np.int16)
    for ch in range(3):
        resultImg_ch = resultImg[:,:,ch]
        if not isTransparent:
            resultImg_ch[destImg] = rgb[ch]
        else:
            resultImg_ch[destImg] = resultImg_ch[destImg] + rgb[ch]
#            resultImg_ch[destImg] = resultImg_ch[destImg] + 255
        if rgbBackground:
            resultImg_ch[destImg_inv] = resultImg_ch[destImg_inv] + rgbBackground[ch]
        resultImg[:,:,ch] = resultImg_ch
        
    resultImg = np.minimum(resultImg, 255)
    resultImg = np.maximum(resultImg, 0)
    resultImg = resultImg.astype(np.uint8)
    return resultImg
    
        
            

def getImgSize(img):
    imgZ = 0
    imgH = img.shape[0]
    imgW = img.shape[1]
    if img.ndim == 3:
        imgZ = img.shape[2]
    return imgH, imgW, imgZ