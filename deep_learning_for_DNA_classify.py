#!/usr/bin/env python
# coding: utf-8

import numpy as np
import os
import tensorflow as tf
import sys
import re
import random

#========================= Model ==============================================
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout
from keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import RMSprop  #from keras.optimizers import RMSprop （python2）
from keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.optimizers import SGD
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

from keras.utils.vis_utils import plot_model


#====================== Read data=================================================
f = open('/home/wuzefeng/Documents/脚本代码/data/kears_data/humanvsran_label.txt', "r") # read label file
lines = f.readlines()
f.close()
dat_y = np.zeros((len(lines),2)) # make a two dimentional data arrary, n() x 2 
for i in range(len(lines)):
    dat_y[i,int(lines[i].rstrip())] = 1

f = open('/home/wuzefeng/Documents/脚本代码/data/kears_data/humanvsran.txt', "r")     # read dna sequences data
lines = f.readlines()
f.close()

#=======================Convert sequences into one-hot matrix====================
def DNA_matrix(seq):
    tem2 = ['[aA]','[cC]','[gG]','[tT]']
    for i in range(len(tem2)):
        ind = [m.start() for m in re.finditer(tem2[i], seq)]
        tem = np.zeros(len(seq),dtype=np.int)
        tem[ind] = 1
        if i==0:
            a = np.zeros((len(seq),4)) # 
            a[...,i] = tem             # a[...,1]代表array第i列; a[1,...]代表array 第i行
    return a

for i in range(len(lines)):
    tem = lines[i].rstrip()
    if i==0:
        dat_x = np.zeros((len(lines),len(tem),4))
    dat_x[i,] = DNA_matrix(tem)

#======================== Split input data into training and testing data============ 
ind = np.arange(20000)
random.shuffle(ind)
x_train=dat_x[ind[0:12000]]
y_train=dat_y[ind[0:12000]]
x_val=dat_x[ind[12001:14001]]
y_val=dat_y[ind[12001:14001]]
x_test=dat_x[14001:20001]
y_test=dat_y[14001:20001]
x_train = x_train.astype('float32')
x_val = x_val.astype('float32')

#========================= model building============================================= 
model=Sequential()
model.add(Conv1D(filters=20,kernel_size=10,strides=1,padding='valid',input_shape=(250,4), activation='relu'))
model.add(MaxPooling1D(pool_size=10, strides=5, padding='same'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='loss', patience=2, mode='min')

#========================model summary==================================================
print(model.summary())
plot_model(model, "/home/wuzefeng/Documents/脚本代码/data/kears_data/my_first_model.png",show_shapes=True) # if error, please run: pip install pydot; pip install pydotplus; sudo apt-get install graphviz

#======================= model train
history = model.fit(x_train, y_train, batch_size=16, epochs=100, verbose=1, validation_data= None,callbacks=[early_stopping])
print(history.history)
#=========================model predict and evluation ===================================================
y_score = model.predict(x_test)
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))

#======================= get parameters =====================================================
weights = model.layers[0].get_weights()
wt=(np.transpose(weights[0][:,:,0]))
wtm=np.transpose(weights[0][:,:,0]).min(axis=0)
wtp=wt-wtm
wtps=np.sum(wtp, axis=0)
print (np.round((wtp/wtps)*100))





