# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:57:08 2020

@author: b9903
"""

import matplotlib.pyplot as plt
import numpy as np

def imshow(img, imgName='img', isFullScreen=False):
    plt.figure()
#    img.dtype
    vmin = 0
    vmax = 1
    if img.dtype == np.bool:
        vmin = 0
        vmax = 1
    elif img.dtype == np.uint8:
        vmin = 0
        vmax = 255
        
    plt.imshow(img, cmap=plt.cm.gray, vmin=vmin, vmax=vmax)
    plt.title('%s: (%gX%gX%g), dtype:%s\nimg range: [%g, %g], imshow range: [%g, %g]'%(imgName, *getImgSize(img), img.dtype, img.max(), img.min(), vmin, vmax))
    if isFullScreen:
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
    return plt
def getImgSize(img):
    imgZ = 0
    imgH = img.shape[0]
    imgW = img.shape[1]
    if img.ndim == 3:
        imgZ = img.shape[2]
    return imgH, imgW, imgZ