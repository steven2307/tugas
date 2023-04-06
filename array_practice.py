#!/usr/bin/env python
# coding: utf-8

# # 1. Create an array and traverse. 

# In[2]:


import numpy as np


# In[5]:


my_array = np.array([1,2,3,4,5])
print (my_array)


# In[6]:


def traversearray(array):
    for i in range(len(array)):
            print (array[i])


# In[7]:


traversearray(my_array)


# # 2. Access individual elements through indexes

# In[8]:


def accsessElements(array,rowIndex):
    if rowIndex >= len(array):
        print('Incorrect Index')
    else:
        print(array[rowIndex])


# In[9]:


accsessElements (my_array,3)


# # 3. Append any value to the array using append() method

# In[10]:


new_myarray = np.append(my_array,[6])
print (new_myarray)


# # 4. Insert value in an array using insert() method

# In[11]:


new_myarray = np.insert(my_array,5,[3,11])
print (new_myarray)


# # 5. Extend python array using extend() method

# In[13]:


my_array = [1,2,3,4,5]
my_array1 = [10,11,12]
my_array.extend(my_array1)
print (my_array)


# 
# # 6. Add items from list into array using fromlist() method

# In[2]:


tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)


# # 7. Remove any array element using remove() method

# In[3]:


my_array.remove(11)
print (my_array)


# # 8. Remove last array element using pop() method

# In[4]:


my_array.pop(9)
print (my_array)


# # 9. Fetch any element through its index using index() method

# In[5]:


index = my_array.index(21)
print(index)


# # 10. Reverse a python array using reverse() method

# In[6]:


my_array.reverse()
print(my_array)


# # 11. Get array buffer information through buffer_info() method

# In[7]:


print(my_array.buffer_info())


# # 12. Check for number of occurrences of an element using count() method

# In[8]:


my_array.append(11)
print(my_array.count(11))
print(my_array)


# # 13. Convert array to string using tostring() method

# In[14]:


from array import *

my_array = array('i', [21, 20, 12, 10, 5, 4, 3, 2, 1, 11])

my_bytes = my_array.tobytes()

print(my_bytes)


# # 14. Convert array to a python list with same elements using tolist() method

# In[11]:


print(my_array.tolist())


# # 16. Slice Elements from an array

# In[16]:


print(my_array[2:5])

