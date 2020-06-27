# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:36:37 2020

@author: mchsiaoj
"""

from .getHighLightImgByRange import getHighLightImgByRange
import numpy as np
from .getStringImg_10 import getStringImg_10
from skimage import transform
#textInfo: {'text': 'I', 'rgb': [200,0,0],'rgb_b': [], 'isTransparent': False, 'fontSize': 5, 'yStart': 50, 'xStart': 50}

def insertTextImgByRange(sourceImg, textInfoList):
    resultImg = np.copy(sourceImg)
    for textInfo in textInfoList:
        stringImg = getStringImg(textInfo)
        resultImg = getHighLightImgByRange(stringImg, resultImg, textInfo['yStart'], textInfo['xStart'], rgb=textInfo['rgb'], isTransparent=textInfo['isTransparent'], rgbBackground=textInfo['rgb_b'])
    return resultImg

def getStringImg(textInfo):
    text = textInfo['text']
    font_size = textInfo['fontSize']
    font_ratio = font_size/10
    stringImg = getStringImg_10(text)
    stringImg2 = transform.rescale(stringImg, font_ratio, order=0).astype(np.bool)
    return stringImg2