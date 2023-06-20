#!/usr/bin/env python
# coding: utf-8

# In[1]:


def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


# In[2]:


print(linearSearch([20,40,30,50,90], 90))

