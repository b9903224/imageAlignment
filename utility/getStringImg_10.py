# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:06:57 2020

@author: b9903
"""

import numpy as np

#text = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'",<.>/? '''

def getStringImg_10(text,font='Minecraft_Regular'):
    L = []
    imgH = 10 # = font_size
    imgW = 10
    img_0 = getBWImgSample(imgH, imgW)
    getRowsAndColsByChar = getCharByFont(font)
    for char in text:
        rows, cols = getRowsAndColsByChar(char)
        img = np.copy(img_0)
        img[rows, cols] = True
        img = pruneImg(img)
        L.append(img)
    stringImg = np.concatenate(L, axis=1)
    return stringImg

def pruneImg(img):
    imgH, imgW = img.shape
    if not np.any(img):
        img = np.zeros((imgH, 5), np.bool)
    else:
        emptyCol = np.zeros((imgH, 1), np.bool)
        x_start, x_end = findMatrixFirstNonZero_LR(img)
        img = img[:,x_start:x_end+1]
        img = np.concatenate((emptyCol,img,emptyCol), axis=1)
    return img

def findMatrixFirstNonZero_LR(img):
    x_start, x_end = 0, 0
    imgH, imgW = img.shape
    for x in range(imgW):
        if any(img[:, x]):
            x_start = x
            break
    for x in range(imgW-1,-1,-1):
        if any(img[:, x]):
            x_end = x
            break
    return x_start, x_end

def getCharByFont(font):
    
    getRowsAndColsByChar = getRowsAndColsByChar_Minecraft_Regular # '`' will be empty
    return getRowsAndColsByChar

def getRowsAndColsByChar_Minecraft_Regular(char):
    if False:
        pass
    elif char == 'a':
        rows = [3,3,3,4,5,5,5,5,6,6,7,7,7,7]
        cols = [2,3,4,5,2,3,4,5,1,5,2,3,4,5]
    elif char == 'b':
        rows = [1,2,3,3,3,4,4,4,5,5,6,6,7,7,7,7]
        cols = [1,1,1,3,4,1,2,5,1,5,1,5,1,2,3,4]
    elif char == 'c':
        rows = [3,3,3,4,4,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,1,5,2,3,4]
    elif char == 'd':
        rows = [1,2,3,3,3,4,4,4,5,5,6,6,7,7,7,7]
        cols = [5,5,2,3,5,1,4,5,1,5,1,5,2,3,4,5]
    elif char == 'e':
        rows = [3,3,3,4,4,5,5,5,5,5,6,7,7,7,7]
        cols = [2,3,4,1,5,1,2,3,4,5,1,2,3,4,5]
    elif char == 'f':
        rows = [1,1,2,3,3,3,3,4,5,6,7]
        cols = [3,4,2,1,2,3,4,2,2,2,2]
    elif char == 'g':
        rows = [3,3,3,3,4,4,5,5,6,6,6,6,7,8,8,8,8]
        cols = [2,3,4,5,1,5,1,5,2,3,4,5,5,1,2,3,4]
    elif char == 'h':
        rows = [1,2,3,3,3,4,4,4,5,5,6,6,7,7]
        cols = [1,1,1,3,4,1,2,5,1,5,1,5,1,5]
    elif char == 'i':
        rows = [1,3,4,5,6,7]
        cols = [1,1,1,1,1,1]
    elif char == 'j':
        rows = [1,3,4,5,6,7,7,8,8,8]
        cols = [5,5,5,5,5,1,5,2,3,4]
    elif char == 'k':
        rows = [1,2,3,3,4,4,5,5,6,6,7,7]
        cols = [1,1,1,4,1,3,1,2,1,3,1,4]
    elif char == 'l':
        rows = [1,2,3,4,5,6,7]
        cols = [1,1,1,1,1,1,2]
    elif char == 'm':
        rows = [3,3,3,4,4,4,5,5,5,6,6,7,7]
        cols = [1,2,4,1,3,5,1,3,5,1,5,1,5]
    elif char == 'n':
        rows = [3,3,3,3,4,4,5,5,6,6,7,7]
        cols = [1,2,3,4,1,5,1,5,1,5,1,5]
    elif char == 'o':
        rows = [3,3,3,4,4,5,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,5,1,5,2,3,4]
    elif char == 'p':
        rows = [3,3,3,4,4,4,5,5,6,6,6,6,7,8]
        cols = [1,3,4,1,2,5,1,5,1,2,3,4,1,1]
    elif char == 'q':
        rows = [3,3,3,4,4,4,5,5,6,6,6,6,7,8]
        cols = [2,3,5,1,4,5,1,5,2,3,4,5,5,5]
    elif char == 'r':
        rows = [3,3,3,4,4,4,5,6,7]
        cols = [1,3,4,1,2,5,1,1,1]
    elif char == 's':
        rows = [3,3,3,3,4,5,5,5,6,7,7,7,7]
        cols = [2,3,4,5,1,2,3,4,5,1,2,3,4]
    elif char == 't':
        rows = [1,2,3,3,3,4,5,6,7]
        cols = [2,2,1,2,3,2,2,2,3]
    elif char == 'u':
        rows = [3,3,4,4,5,5,6,6,7,7,7,7]
        cols = [1,5,1,5,1,5,1,5,2,3,4,5]
    elif char == 'v':
        rows = [3,3,4,4,5,5,6,6,7]
        cols = [1,5,1,5,1,5,2,4,3]
    elif char == 'w':
        rows = [3,3,4,4,5,5,5,6,6,6,7,7,7,7]
        cols = [1,5,1,5,1,3,5,1,3,5,2,3,4,5]
    elif char == 'x':
        rows = [3,3,4,4,5,6,6,7,7]
        cols = [1,5,2,4,3,2,4,1,5]
    elif char == 'y':
        rows = [3,3,4,4,5,5,6,6,6,6,7,8,8,8,8]
        cols = [1,5,1,5,1,5,2,3,4,5,5,1,2,3,4]
    elif char == 'z':
        rows = [3,3,3,3,3,4,5,6,7,7,7,7,7]
        cols = [1,2,3,4,5,4,3,2,1,2,3,4,5]
    elif char == 'A':
        rows = [1,1,1,2,2,3,3,3,3,3,4,4,5,5,6,6,7,7]
        cols = [2,3,4,1,5,1,2,3,4,5,1,5,1,5,1,5,1,5]
    elif char == 'B':
        rows = [1,1,1,1,2,2,3,3,3,3,4,4,5,5,6,6,7,7,7,7]
        cols = [1,2,3,4,1,5,1,2,3,4,1,5,1,5,1,5,1,2,3,4]
    elif char == 'C':
        rows = [1,1,1,2,2,3,4,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,1,1,1,5,2,3,4]
    elif char == 'D':
        rows = [1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,7,7]
        cols = [1,2,3,4,1,5,1,5,1,5,1,5,1,5,1,2,3,4]
    elif char == 'E':
        rows = [1,1,1,1,1,2,3,3,3,4,5,6,7,7,7,7,7]
        cols = [1,2,3,4,5,1,1,2,3,1,1,1,1,2,3,4,5]
    elif char == 'F':
        rows = [1,1,1,1,1,2,3,3,3,4,5,6,7]
        cols = [1,2,3,4,5,1,1,2,3,1,1,1,1]
    elif char == 'G':
        rows = [1,1,1,1,2,3,3,3,4,4,5,5,6,6,7,7,7]
        cols = [2,3,4,5,1,1,4,5,1,5,1,5,1,5,2,3,4]
    elif char == 'H':
        rows = [1,1,2,2,3,3,3,3,3,4,4,5,5,6,6,7,7]
        cols = [1,5,1,5,1,2,3,4,5,1,5,1,5,1,5,1,5]
    elif char == 'I':
        rows = [1,1,1,2,3,4,5,6,7,7,7]
        cols = [1,2,3,2,2,2,2,2,1,2,3]
    elif char == 'J':
        rows = [1,2,3,4,5,6,6,7,7,7]
        cols = [5,5,5,5,5,1,5,2,3,4]
    elif char == 'K':
        rows = [1,1,2,2,3,3,3,4,4,5,5,6,6,7,7]
        cols = [1,5,1,4,1,2,3,1,4,1,5,1,5,1,5]
    elif char == 'L':
        rows = [1,2,3,4,5,6,7,7,7,7,7]
        cols = [1,1,1,1,1,1,1,2,3,4,5]
    elif char == 'M':
        rows = [1,1,2,2,2,2,3,3,3,4,4,5,5,6,6,7,7]
        cols = [1,5,1,2,4,5,1,3,5,1,5,1,5,1,5,1,5]
    elif char == 'N':
        rows = [1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,7,7]
        cols = [1,5,1,2,5,1,3,5,1,4,5,1,5,1,5,1,5]
    elif char == 'O':
        rows = [1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,5,1,5,1,5,1,5,2,3,4]
    elif char == 'P':
        rows = [1,1,1,1,2,2,3,3,3,3,4,5,6,7]
        cols = [1,2,3,4,1,5,1,2,3,4,1,1,1,1]
    elif char == 'Q':
        rows = [1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,5,1,5,1,5,1,4,2,3,5]
    elif char == 'R':
        rows = [1,1,1,1,2,2,3,3,3,3,4,4,5,5,6,6,7,7]
        cols = [1,2,3,4,1,5,1,2,3,4,1,5,1,5,1,5,1,5]
    elif char == 'S':
        rows = [1,1,1,1,2,3,3,3,4,5,6,6,7,7,7]
        cols = [2,3,4,5,1,2,3,4,5,5,1,5,2,3,4]
    elif char == 'T':
        rows = [1,1,1,1,1,2,3,4,5,6,7]
        cols = [1,2,3,4,5,3,3,3,3,3,3]
    elif char == 'U':
        rows = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,7]
        cols = [1,5,1,5,1,5,1,5,1,5,1,5,2,3,4]
    elif char == 'V':
        rows = [1,1,2,2,3,3,4,4,5,5,6,6,7]
        cols = [1,5,1,5,1,5,1,5,2,4,2,4,3]
    elif char == 'W':
        rows = [1,1,2,2,3,3,4,4,5,5,5,6,6,6,6,7,7]
        cols = [1,5,1,5,1,5,1,5,1,3,5,1,2,4,5,1,5]
    elif char == 'X':
        rows = [1,1,2,2,3,4,4,5,5,6,6,7,7]
        cols = [1,5,2,4,3,2,4,1,5,1,5,1,5]
    elif char == 'Y':
        rows = [1,1,2,2,3,4,5,6,7]
        cols = [1,5,2,4,3,3,3,3,3]
    elif char == 'Z':
        rows = [1,1,1,1,1,2,3,4,5,6,7,7,7,7,7]
        cols = [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5]
    elif char == '0':
        rows = [1,1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,4,5,1,3,5,1,2,5,1,5,2,3,4]
    elif char == '1':
        rows = [1,2,2,3,4,5,6,7,7,7,7,7]
        cols = [3,2,3,3,3,3,3,1,2,3,4,5]
    elif char == '2':
        rows = [1,1,1,2,2,3,4,4,5,6,6,7,7,7,7,7]
        cols = [2,3,4,1,5,5,3,4,2,1,5,1,2,3,4,5]
    elif char == '3':
        rows = [1,1,1,2,2,3,4,4,5,6,6,7,7,7]
        cols = [2,3,4,1,5,5,3,4,5,1,5,2,3,4]
    elif char == '4':
        rows = [1,1,2,2,3,3,4,4,5,5,5,5,5,6,7]
        cols = [4,5,3,5,2,5,1,5,1,2,3,4,5,5,5]
    elif char == '5':
        rows = [1,1,1,1,1,2,3,3,3,3,4,5,6,6,7,7,7]
        cols = [1,2,3,4,5,1,1,2,3,4,5,5,1,5,2,3,4]
    elif char == '6':
        rows = [1,1,2,3,4,4,4,4,5,5,6,6,7,7,7]
        cols = [3,4,2,1,1,2,3,4,1,5,1,5,2,3,4]
    elif char == '7':
        rows = [1,1,1,1,1,2,2,3,4,5,6,7]
        cols = [1,2,3,4,5,1,5,5,4,3,3,3]
    elif char == '8':
        rows = [1,1,1,2,2,3,3,4,4,4,5,5,6,6,7,7,7]
        cols = [2,3,4,1,5,1,5,2,3,4,1,5,1,5,2,3,4]
    elif char == '9':
        rows = [1,1,1,2,2,3,3,4,4,4,4,5,6,7,7]
        cols = [2,3,4,1,5,1,5,2,3,4,5,5,4,2,3]
    elif char == '`':
        rows = []
        cols = []
    elif char == '~':
        rows = [1,1,1,2,2,2]
        cols = [2,3,6,1,4,5]
    elif char == '!':
        rows = [1,2,3,4,5,7]
        cols = [1,1,1,1,1,1]
    elif char == '@':
        rows = [1,1,1,1,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,7,7,7,7]
        cols = [2,3,4,5,1,6,1,3,4,6,1,3,4,6,1,3,4,5,6,1,2,3,4,5]
    elif char == '#':
        rows = [1,1,2,2,3,3,3,3,3,4,4,5,5,5,5,5,6,6,7,7]
        cols = [2,4,2,4,1,2,3,4,5,2,4,1,2,3,4,5,2,4,2,4]
    elif char == '$':
        rows = [1,2,2,2,2,3,4,4,4,5,6,6,6,6,7]
        cols = [3,2,3,4,5,1,2,3,4,5,1,2,3,4,3]
    elif char == '%':
        rows = [1,1,2,2,3,4,5,6,6,7,7]
        cols = [1,5,1,4,4,3,2,2,5,1,5]
    elif char == '^':
        rows = [1,2,2,3,3]
        cols = [3,2,4,1,5]
    elif char == '&':
        rows = [1,2,2,3,4,4,4,5,5,5,6,6,7,7,7]
        cols = [3,2,4,3,2,3,5,1,3,4,1,4,2,3,5]
    elif char == '*':
        rows = [3,3,4,4,5,5]
        cols = [1,4,2,3,1,4]
    elif char == '(':
        rows = [1,1,2,3,4,5,6,7,7]
        cols = [3,4,2,1,1,1,2,3,4]
    elif char == ')':
        rows = [1,1,2,3,4,5,6,7,7]
        cols = [1,2,3,4,4,4,3,1,2]
    elif char == '-':
        rows = [4,4,4,4,4]
        cols = [1,2,3,4,5]
    elif char == '_':
        rows = [8,8,8,8,8]
        cols = [1,2,3,4,5]
    elif char == '=':
        rows = [3,3,3,3,3,6,6,6,6,6]
        cols = [1,2,3,4,5,1,2,3,4,5]
    elif char == '+':
        rows = [2,3,4,4,4,4,4,5,6]
        cols = [3,3,1,2,3,4,5,3,3]
    elif char == '[':
        rows = [1,1,1,2,3,4,5,6,7,7,7]
        cols = [1,2,3,1,1,1,1,1,1,2,3]
    elif char == '{':
        rows = [1,1,2,3,4,5,6,7,7]
        cols = [3,4,2,2,1,2,2,3,4]
    elif char == ']':
        rows = [1,1,1,2,3,4,5,6,7,7,7]
        cols = [1,2,3,3,3,3,3,3,1,2,3]
    elif char == '}':
        rows = [1,1,2,3,4,5,6,7,7]
        cols = [1,2,3,3,4,3,3,1,2]
    elif char == '\\':
        rows = [1,2,3,4,5,6,7]
        cols = [1,2,2,3,4,4,5]
    elif char == '|':
        rows = [1,2,3,5,6,7]
        cols = [1,1,1,1,1,1]
    elif char == ';':
        rows = [2,3,6,7,8]
        cols = [1,1,1,1,1]
    elif char == ':':
        rows = [2,3,6,7]
        cols = [1,1,1,1]
    elif char == '\'':
        rows = [1,2,3]
        cols = [2,2,1]
    elif char == '"':
        rows = [1,1,2,2,3,3]
        cols = [2,4,2,4,1,3]
    elif char == ',':
        rows = [6,7,8]
        cols = [1,1,1]
    elif char == '<':
        rows = [1,2,3,4,5,6,7]
        cols = [4,3,2,1,2,3,4]
    elif char == '.':
        rows = [6,7]
        cols = [1,1]
    elif char == '>':
        rows = [1,2,3,4,5,6,7]
        cols = [1,2,3,4,3,2,1]
    elif char == '/':
        rows = [1,2,3,4,5,6,7]
        cols = [5,4,4,3,2,2,1]
    elif char == '?':
        rows = [1,1,1,2,2,3,4,5,7]
        cols = [2,3,4,1,5,5,4,3,3]
    elif char == ' ':
        rows = []
        cols = []
    else: # copy from '?'
        rows = [1,1,1,2,2,3,4,5,7]
        cols = [2,3,4,1,5,5,4,3,3]
    return rows, cols

def getBWImgSample(imgH, imgW):
    img = np.zeros((imgH, imgW), np.bool)
    return img

# generate char to array index

# test cell2mat like Matlab
#a = np.array([[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])],[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])],[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])]], np.bool)
#b = np.array([[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])],[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])],[random.choice([0, 1]),random.choice([0, 1]),random.choice([0, 1])]], np.bool)
#L = []
#L.append(a)
#L.append(b)
#result = np.concatenate(L, axis=1)
#utility.imshow(a)
#utility.imshow(b)
#utility.imshow(result)
    