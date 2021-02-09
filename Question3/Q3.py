#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Activation,Dropout
from tensorflow.keras.models import Model
#load data
x_train_data = pd.read_table('C:/Users/47634/Desktop/AY20_MBDS_questions/Question 3/train_data.txt')
x_train = np.array(x_train_data)
y_train_truth = pd.read_table('C:/Users/47634/Desktop/AY20_MBDS_questions/Question 3/train_truth.txt')
y_train = np.array(y_train_truth)
x_test_data = pd.read_table('C:/Users/47634/Desktop/AY20_MBDS_questions/Question 3/test_data.txt')
x_test = np.array(x_test_data)
print(x_train)
print(y_train)
print(x_test)


# In[9]:


#Model training 
input_layer = Input(shape=(x_train.shape[1],))
hidden_layer_1 = Dense(4, activation='relu')(input_layer)
hidden_layer_2 = Dense(4, activation='relu')(hidden_layer_1)
output_layer = Dense(1)(hidden_layer_2)
model = Model(inputs=input_layer, outputs=output_layer)
model.compile(loss="mean_squared_error" , optimizer="Adam", metrics=["mean_squared_error"])
model.summary()


# In[14]:


history = model.fit(x_train, y_train, batch_size=10, epochs=10, verbose=1, validation_split=0.2)
y_test = model.predict(x_test)
f=open('C://Users/47634/Desktop/NTU TEST/Question3/test_predicted.txt', 'w+', encoding='utf8')
print('y',file=f)
for i in range(len(y_test)):
        print(y_test[i][0],file=f)
f.close()


# In[ ]:




