#!/usr/bin/env python
# coding: utf-8

# In[1]:


import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())


# In[2]:


customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())


# In[3]:


print(customQueue.get())


# In[4]:


print(customQueue.qsize())

