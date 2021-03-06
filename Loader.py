# -*- coding: utf-8 -*-
"""Loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eR9v0ijYI_9ExtVcBlGESjcIrl2oSPNT
"""

import matplotlib.pyplot as plt
import cv2
import glob, os, shutil
from keras import layers
from keras import models
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import keras
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, image 
from keras.models import load_model
from typing import Union
from torch.nn import Module
from keras.models import Model

class Loader:
    def __init__(self, model_number: int, base_path: str):
        self.model_number = model_number
        self.base_path = base_path
        self.model = self.load_net()

    def load_net(self) -> Union[Model, Module]:
        return load_model(self.base_path + '/Models/Model'+ str(self.model_number) + '.h5')

    
    def predict(self, video_name) -> float:
        img = 0
        try:
          img = image.load_img( self.base_path +  '/Test_Data_Raw/real/' + video_name + '.jpg', target_size = (480, 270))
        except:
          img = image.load_img( self.base_path  +  '/Test_Data_Raw/spoof/' + video_name + '.jpg', target_size = (480, 270))
        finally:
          img = image.img_to_array(img)
          img = np.expand_dims(img, axis = 0)
          return  self.model.predict(img)[0][0]