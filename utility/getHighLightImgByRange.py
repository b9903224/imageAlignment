# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:16:40 2020

@author: b9903
"""

import numpy as np

def getHighLightImgByRange(destImg, sourceImg, yStart, xStart, rgb=[255, 0, 0], isTransparent=False, rgbBackground=[]):

    
    resultImg = iniResultImg(sourceImg)
#    destImg_inv = np.invert(destImg)
    
    imgH_src, imgW_src, imgZ_src = getImgSize(sourceImg)
    imgH_dest, imgW_dest, imgZ_dest = getImgSize(destImg)
    yEnd = min(yStart+imgH_dest-1, imgH_src-1)
    xEnd = min(xStart+imgW_dest-1, imgW_src-1)
    destImg_sub = destImg[0:yEnd-yStart+1, 0:xEnd-xStart+1]
    resultImg_sub = resultImg[yStart:yEnd+1,xStart:xEnd+1,:]
    resultImg_sub = resultImg_sub.astype(np.int16)
    destImg_sub_inv = np.invert(destImg_sub)
    for ch in range(3):
        resultImg_sub_ch = resultImg_sub[:,:,ch]
        if not isTransparent:
            resultImg_sub_ch[destImg_sub] = rgb[ch]
        else:
            resultImg_sub_ch[destImg_sub] = resultImg_sub_ch[destImg_sub] + rgb[ch]
#            resultImg_ch[destImg] = resultImg_ch[destImg] + 255
        if rgbBackground:
            resultImg_sub_ch[destImg_sub_inv] = resultImg_sub_ch[destImg_sub_inv] + rgbBackground[ch]
        resultImg_sub[:,:,ch] = resultImg_sub_ch
    
    resultImg_sub = finalizeResultImg(resultImg_sub)
    resultImg[yStart:yEnd+1,xStart:xEnd+1,:] = resultImg_sub
    return resultImg

def finalizeResultImg(resultImg):
    resultImg = np.minimum(resultImg, 255)
    resultImg = np.maximum(resultImg, 0)
    resultImg = resultImg.astype(np.uint8)    
    return resultImg

def iniResultImg(sourceImg):
    resultImg = np.copy(sourceImg)
    if resultImg.dtype == np.bool:
        resultImg = resultImg.astype(np.uint8)*255
    imgH, imgW, imgZ = getImgSize(resultImg)
    if imgZ == 0:
        resultImg = np.dstack((resultImg, resultImg, resultImg))
#    resultImg = resultImg.astype(np.float)
    return resultImg

def getImgSize(img):
    imgZ = 0
    imgH = img.shape[0]
    imgW = img.shape[1]
    if img.ndim == 3:
        imgZ = img.shape[2]
    return imgH, imgW, imgZ