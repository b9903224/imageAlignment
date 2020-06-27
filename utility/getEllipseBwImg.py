# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:32:57 2020

@author: mchsiaoj
"""
import numpy as np

def getEllipseBwImg(imgH, imgW, centerY, centerX, radiusY, radiusX, theta=0, backgroundImg=[]):
    x = np.linspace(0, imgW-1, imgW)
    y = np.linspace(0, imgH-1, imgH)
    
#    [X, Y] = meshgrid(1 : imgW, 1 : imgH); # Matlab
    X, Y = np.meshgrid(x, y)
    
    X2 = rotateByTheta_X(X, Y, theta)
    Y2 = rotateByTheta_Y(X, Y, theta)
    
    centerX2 = rotateByTheta_X(centerX, centerY, theta);
    centerY2 = rotateByTheta_Y(centerX, centerY, theta);
    
#    ellipseBwImg = ((Y2 - centerY2).^2./radiusY^2 + (X2 - centerX2).^2./radiusX^2) <=1; # Matlab
    ellipseBwImg = ((Y2 - centerY2)**2/radiusY**2 + (X2 - centerX2)**2/radiusX**2) <=1
    if backgroundImg !=[]:
        ellipseBwImg = np.logical_or(ellipseBwImg, backgroundImg)
    return ellipseBwImg
    
def rotateByTheta_X(X, Y, theta):
#    X2 = X*cosd(theta) + Y*sind(theta); # Matlab
    X2 = X*cosd(theta) + Y*sind(theta)
    return X2

def rotateByTheta_Y(X, Y, theta):
#    Y2 = -X*sind(theta) + Y*cosd(theta); # Matlab
    Y2 = -X*sind(theta) + Y*cosd(theta)
    return Y2
    
def cosd(theta):
    return np.cos(theta*np.pi/180)

def sind(theta):
    return np.sin(theta*np.pi/180)

