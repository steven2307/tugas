#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


# In[2]:


def zoKnapsack(items, capacity, currentIndex):
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapsack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0


# In[3]:


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]


# In[4]:


print(zoKnapsack(items, 7, 0))

