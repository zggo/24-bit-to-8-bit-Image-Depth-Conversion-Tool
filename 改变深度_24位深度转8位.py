# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:47:15 2022

24位深度转8位
"""
import os
import cv2
bacepath = "changecolor/"
savepath = 'changecolor/'

f_n  = os.listdir(bacepath)
print(f_n)
for n in f_n:
    imdir = bacepath + '\\' + n
    print(n)
    img = cv2.imread(imdir)
    cropped = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(savepath + '\\' + n.split('.')[0]+'.png', cropped)#NOT CAHNGE THE TYPE

