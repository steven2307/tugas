#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1,s2, index1, index2+1)
        op2 = findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)


# In[2]:


print(findLCS("elephant", "eretpat", 0, 0))

