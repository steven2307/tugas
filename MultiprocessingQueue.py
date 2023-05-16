#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())

