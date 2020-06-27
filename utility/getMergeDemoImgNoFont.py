# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 00:07:14 2020

@author: b9903
"""

import numpy as np
from skimage import transform
#from .getStringImg_20 import getStringImg_20
from .getStringImg_10 import getStringImg_10
from .getHighLightImgByRange import getHighLightImgByRange

def getMergeDemoImgNoFont(rgb,rgb_b,rgb_demo,
                          row_num,col_num,font_size,gap_ver,gap_hoz,
                          descp_height,imgH,imgW,
                          img_list,descp_text,descp_test_start_y,descp_test_start_x):
    font_ratio = font_size/10
    mergedDemoImg = iniMergedDemoImg(row_num * (imgH + gap_ver) + descp_height,
                                     col_num * (imgW + gap_hoz), rgb_demo)
    mergedDemoImg = insert_img_list(mergedDemoImg, img_list, imgH, imgW, gap_ver, gap_hoz, font_ratio)
    mergedDemoImg = insert_descp_text(mergedDemoImg, descp_text, imgH, imgW,
                                      descp_test_start_y, descp_test_start_x, 
                                      font_size, font_ratio)
    mergedDemoImg = finalizeResultImg(mergedDemoImg)
    return mergedDemoImg

def insert_descp_text(mergedDemoImg, descp_text, imgH, imgW,
                      descp_test_start_y, descp_test_start_x, 
                      font_size, font_ratio):
    
    for row_num, descp_row in enumerate(descp_text):
        y0 = descp_test_start_y[row_num]
        x = descp_test_start_x[row_num]
        for col_num, descp in enumerate(descp_row):
            if not descp:
                continue
            y = y0 + font_size*col_num
            descp_text = descp['text']
            descp_rgb = descp['rgb']
            descp_rgb_b = descp['rgb_b']
            if not descp_text:
                continue
            stringImg = getStringImg(descp_text, font_ratio)
            mergedDemoImg = getHighLightImgByRange(stringImg, mergedDemoImg, y, x, rgb=descp_rgb, isTransparent=False, rgbBackground=descp_rgb_b)
            
    return mergedDemoImg

def insert_img_list(mergedDemoImg, img_list, imgH, imgW, gap_ver, gap_hoz, font_ratio):
    for row_num, img_row in enumerate(img_list):
        y_img = row_num * imgH + (row_num + 1) * gap_ver
        y_title = row_num * (imgH + gap_ver)
        for col_num, img in enumerate(img_row):
            if not img:
                continue
            x_img = col_num * (imgW + gap_hoz)
            x_title = col_num * (imgW + gap_hoz)
            img_img = img['img']
            img_title = img['title']
            img_rgb = img['rgb']
            img_rgb_b = img['rgb_b']
            if img_img.ndim == 2:
                if img_img.dtype == np.bool:
                    img_img = img_img.astype(np.uint8) * 255
                    for ch in range(3):
                        mergedDemoImg[y_img:y_img+imgH, x_img:x_img+imgW, ch] = img_img
                if img_img.dtype == np.uint8:
                    for ch in range(3):
                        mergedDemoImg[y_img:y_img+imgH, x_img:x_img+imgW, ch] = img_img
            elif img_img.ndim == 3:
                for ch in range(3):
                    mergedDemoImg[y_img:y_img+imgH, x_img:x_img+imgW, ch] = img_img[...,ch]
            if len(img_title) == 0:
                continue
            else:
                stringImg = getStringImg(img_title, font_ratio)
                mergedDemoImg = getHighLightImgByRange(stringImg, mergedDemoImg, y_title, x_title, rgb=img_rgb, isTransparent=False, rgbBackground=img_rgb_b)
            
    return mergedDemoImg

def getStringImg(text, font_ratio):
    stringImg = getStringImg_10(text)
    stringImg2 = transform.rescale(stringImg, font_ratio, order=0).astype(np.bool)
    return stringImg2

def iniMergedDemoImg(imgH, imgW, rgb_demo):
    mergedDemoImg = np.zeros((imgH, imgW, 3), dtype=np.uint8)
    for ch in range(3):
        mergedDemoImg[..., ch] = rgb_demo[ch]
        
    return mergedDemoImg

def finalizeResultImg(resultImg):
    resultImg = np.minimum(resultImg, 255)
    resultImg = np.maximum(resultImg, 0)
    resultImg = resultImg.astype(np.uint8)    
    return resultImg






