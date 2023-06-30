#!/usr/bin/env python
# coding: utf-8

# In[1]:


def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break


# In[2]:


coins = [1,2,5,20,50,100]


# In[3]:


coinChange(327, coins)

