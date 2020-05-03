#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tensorflow.python.keras.preprocessing.image import ImageDataGenerator 
import numpy as np
import glob
from PIL import *
import PIL
from scipy import ndimage
def augment_data(path,save_path):
    #datagen=ImageDataGenerator(rotation_range=10, width_shift_range=0.1,height_shift_range=0.1,zoom_range=0.1,vertical_flip=True, horizontal_flip=True)
    datagen=ImageDataGenerator(rotation = 360, width_shift_range=100,height_shift_range=100)
    file_paths = glob.glob(path)
    for image_path in file_paths:
        #image = np.expand_dims(ndimage.imread(image_path), 0)
        image = Image.open(image_path)
        image = np.expand_dims(image, 0)
        datagen.fit(image)
        for x, val in zip(datagen.flow(image,
            save_to_dir=save_path,     #this is where we figure out where to save
             save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
            save_format='jpeg'),range(10)) :     # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
            pass
augment_data("C:\MyLearnings\DeepLearning\\Currency\\Dataset\\Resizedcurrency\\Augmentdata\\train\\Rs50\\*.jpg","C:\MyLearnings\DeepLearning\\Currency\\Dataset\\Resizedcurrency\\Augmentdata\\Aug\\train\\Rs50\\zca_whitening\\",)
augment_data("C:\MyLearnings\DeepLearning\\Currency\\Dataset\\Resizedcurrency\\Augmentdata\\train\\Rs50\\*.jpeg","C:\MyLearnings\DeepLearning\\Currency\\Dataset\\Resizedcurrency\\Augmentdata\\Aug\\train\\Rs50\\zca_whitening\\",)


# In[ ]:




