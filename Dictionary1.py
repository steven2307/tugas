#!/usr/bin/env python
# coding: utf-8

# In[17]:


myDict = {'name':'Edy','age': 26}
myDict['address'] = 'London'
print(myDict)


# In[18]:


myDict['age']=27
print(myDict)


# In[19]:


def traverseDict(dict):
    for key in dict:
        print(key,dict[key])
traverseDict(myDict)


# In[20]:


print(myDict)


# In[21]:


def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'
print(searchDict(myDict, 27))


# In[22]:


myDict.pop('name')


# In[23]:


print(myDict)


# In[28]:


myDict = {'eooooa' : 1,'aas' : 2,'udd' : 3, 'sseo' : 4, 'werwi' : 5}
print(sorted(myDict, key=len))


# In[29]:


print(myDict)


# In[30]:


myDict.clear()


# In[31]:


print(myDict)


# In[32]:


myDict = {'name' : 'Edy','age' : 26}


# In[33]:


print(myDict)


# In[34]:


dict = myDict.copy()


# In[35]:


print(dict)


# In[39]:


newDict = {}.fromkeys([1,2,3],676)
print(newDict)


# In[40]:


print(myDict.get('name', 26))


# In[41]:


print(myDict.get('city', 27))


# In[43]:


print(myDict.get('city'))


# In[45]:


print(myDict.items())


# In[46]:


print(myDict.keys())


# In[47]:


print(myDict.values())


# In[48]:


print(myDict.popitem())


# In[49]:


print(myDict)


# In[51]:


print(myDict.setdefault('name','added'))


# In[52]:


print(myDict)


# In[57]:


print(myDict.setdefault('name1','added'))


# In[58]:


print(myDict)


# In[59]:


print(myDict.pop('name1','not'))


# In[60]:


print(myDict)


# In[61]:


newDict = {'a':1,'b':2,'c':3}
myDict.update(newDict)
print(myDict)


# In[ ]:




