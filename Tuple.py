#!/usr/bin/env python
# coding: utf-8

# In[3]:


newTuple = ('a','b','c','d','e')
newTuple1 = tuple('abcde')
print(newTuple)


# In[4]:


print(newTuple1)


# In[11]:


print(newTuple[0::2])


# In[12]:


print(newTuple[0:2])


# In[9]:


for i in newTuple:
    print(i)


# In[13]:


for index in range(len(newTuple)):
    print(newTuple[index])


# In[14]:


print('a' in newTuple)


# In[15]:


print('t' in newTuple)


# In[ ]:


def searchInTuple(pTuple,element):
    for i in Tuple

