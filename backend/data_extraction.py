import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

def load_images_from_folder(folder):
  train_data=[]
  for f in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,f),cv2.IMREAD_GRAYSCALE)
    img =- img
    if img is not None:
        ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        ret,ctrs,ret = cv2.findCountours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        count = sorted(ctrs,key = lambda ctr: cv2.boundingRect(ctr)[0])
        w = int(28)
        h = int(28)
        maxi = 0
        for c in count:
          x,y,w,h = cv2.boundingRect(c)
          maxi = max(w*h,maxi)
          if maxi == w*h:
            x_max=x
            y_max=y
            w_max=w
            h_max=h
          im_crop= thresh[y_max:y_max+h_max+10, x_max:x_max+w_max+10]
          im_resize = cv2.resize(im_crop,(28,28))
          im_resize=np.reshape(im_resize,(784,1))
          train_data.append(im_resize)
  return train_data
        