# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:57:02 2021

@author: timka
"""

import cv2 as cv

import numpy as np

fn = 'p1.png'
img = cv.imread(fn)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array((70, 70, 70), np.uint8)

upper = np.array((150,255,255), np.uint8)

mask = cv.inRange(hsv, lower, upper)
result = cv.bitwise_and(img, img, mask = mask)

cv.imshow('frame', img)
cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows() 