#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None


# In[2]:


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())


# In[3]:


customQueue.delete()

