#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[10]:


twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)


# In[13]:


newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]],axis=0)
print(newTwoDArray)


# In[14]:


print(len(twoDArray))


# In[17]:


newTwoDArray = np.append(twoDArray,[[1,2,3,4]],axis=0)
print(newTwoDArray)


# In[18]:


print(len(newTwoDArray))


# In[19]:


print(len(newTwoDArray[0]))


# In[23]:


def accsessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])


# In[28]:


accsessElements(newTwoDArray,1,2)


# In[32]:


def traverseTDArray(array):
    for i in range(len(array)):
        for j in range (len(array[0])):
            print(array[i][j])


# In[33]:


traverseTDArray(twoDArray)


# In[42]:


def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is locateed index ' +str(i)+" "+str(j)
    return 'The element is not found'


# In[43]:


print(twoDArray)


# In[44]:


print(searchTDArray(twoDArray,12))


# In[45]:


newTDArray = np.delete(twoDArray,2,axis=0)
print(newTDArray)


# In[46]:


print(twoDArray)


# In[ ]:




