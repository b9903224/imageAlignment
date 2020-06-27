# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:30:07 2020

@author: b9903
"""

import numpy as np
#import matplotlib.pyplot as plt
#from skimage import io
from PIL import ImageFont, ImageDraw, Image

text = r'''abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?'''

def getFontTemplateImg(imgH, imgW, font_path, x_ori=0, y_ori=0):
    img = getImgRGBSample(imgH, imgW)
    font_size = imgH
    font_rgb = [255,255,255]
    font = ImageFont.truetype(font_path, font_size)
    frame = Image.fromarray(img)
    draw = ImageDraw.Draw(frame)
    draw.text((x_ori, y_ori), text, tuple(font_rgb), font=font)
    img_text = np.array(frame)
    img_text = img_text[:,:,0]
    
    return img_text
    
def getImgRGBSample(imgH, imgW):
    img = np.zeros((imgH, imgW), np.uint8)
    img.fill(0)
    img = np.dstack((img,img,img))
    return img

def getImgSample(imgH, imgW):
    img_bw = np.zeros((imgH, imgW), np.bool)
    img_bw.fill(True)
    img_gray = np.zeros((imgH, imgW), np.uint8)
    img_gray.fill(127)
    img_rgb = np.zeros((imgH, imgW), np.uint8)
    img_rgb.fill(0)
    img_rgb = np.dstack((img_rgb,img_rgb,img_rgb))    
    return img_bw, img_gray, img_rgb


