# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:39:15 2019

@author: b9903
"""

import numpy as np
from PIL import ImageFont, ImageDraw, Image

'''
font_background_rgb: unused
'''
#import time
#start = time.time()
#time.sleep(5.5)
#end = time.time()
#print(end - start)



##
def getMergedDemoImg(row_num, col_num, imgH, imgW,
                     img_list, title_list, gap_ver, gap_hoz,
                     font_path, font_size, font_rgb, font_background_rgb,
                     demo_background_rgb, append_height, descp_text,
                     descp_test_start_y, descp_test_start_x):
    
    mergedDemoImg = iniMergedDemoImg(row_num * (imgH + gap_ver) + append_height,
                                     col_num * (imgW + gap_hoz), demo_background_rgb)
    mergedDemoImg = insert_img_list(mergedDemoImg, img_list, imgH, imgW, gap_ver, gap_hoz)
    
    
    # insert text
    font = get_font(font_path, font_size)
    mergedDemoImg = insert_title_list(mergedDemoImg, title_list, imgH, imgW, gap_ver, gap_hoz,
                                      font_path, font_size, font_rgb, font)
    mergedDemoImg = insert_descp_text(mergedDemoImg, descp_text, imgH, imgW,
                                      descp_test_start_y, descp_test_start_x,
                                      font_size, font_rgb, font)
    
    return mergedDemoImg

##
def insert_descp_text(mergedDemoImg, descp_text, imgH, imgW,
                      descp_test_start_y, descp_test_start_x, 
                      font_size, font_rgb, font):
    
    frame = Image.fromarray(mergedDemoImg)
    draw = ImageDraw.Draw(frame)
    
    for row_num, descp_row in enumerate(descp_text):
        y0 = descp_test_start_y[row_num]
        x = descp_test_start_x[row_num]
        for col_num, descp in enumerate(descp_row):
            y = y0 + font_size*col_num
#            print(y)
            if len(descp) == 0:
                continue
            draw.text((x,y), descp, tuple(font_rgb), font=font)
    
    mergedDemoImg = np.array(frame)
    return mergedDemoImg

##
def insert_title_list(mergedDemoImg, title_list, imgH, imgW, gap_ver, gap_hoz,
                      font_path, font_size, font_rgb, font):
    
    frame = Image.fromarray(mergedDemoImg)
    draw = ImageDraw.Draw(frame)
    
    for row_num, title_row in enumerate(title_list):
        y = row_num * (imgH + gap_ver)
        for col_num, title in enumerate(title_row):
            x = col_num * (imgW + gap_hoz)
            if len(title) == 0:
                continue
            draw.text((x,y), title, tuple(font_rgb), font=font)
    
    mergedDemoImg = np.array(frame)
    return mergedDemoImg

##
def get_font(font_path, font_size):
    
    if len(font_path) == 0:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)
        
    return font

##
def insert_img_list(mergedDemoImg, img_list, imgH, imgW, gap_ver, gap_hoz):
    
    for row_num, img_row in enumerate(img_list):
        y = row_num * imgH + (row_num + 1) * gap_ver
        
        for col_num, img in enumerate(img_row):
            if len(img) == 0:
                continue
            
            x = col_num * (imgW + gap_hoz)
            
            if img.ndim == 2:
                if img.dtype == np.bool:
                    img = img.astype(np.uint8) * 255
                    for ch in range(3):
                        mergedDemoImg[y:y+imgH, x:x+imgW, ch] = img
                if img.dtype == np.uint8:
                    for ch in range(3):
                        mergedDemoImg[y:y+imgH, x:x+imgW, ch] = img
            elif img.ndim == 3:
                for ch in range(3):
                    mergedDemoImg[y:y+imgH, x:x+imgW, ch] = img[...,ch]
                
                
                    
    return mergedDemoImg
            
##
def iniMergedDemoImg(imgH, imgW, demo_background_rgb):
    
    mergedDemoImg = np.zeros((imgH, imgW, 3), dtype=np.uint8)
    for ch in range(3):
        mergedDemoImg[..., ch] = demo_background_rgb[ch]
        
    return mergedDemoImg




