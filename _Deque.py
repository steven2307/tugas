#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)


# In[2]:


customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)


# In[3]:


print(customQueue.clear())


# In[4]:


print(customQueue)

