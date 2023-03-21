#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import time
 
def find_solution(n):
  # seed the random number generator with the current time
  random.seed(time.time())
  # randomly select a number between 1 and n and return it as the solution
  return random.randint(1, n)
 
def main():
  n = 10  # the range of possible solutions is 1 to n
  print("Solution:", find_solution(n))
 
if __name__ == '__main__':
  main()


# In[ ]:




