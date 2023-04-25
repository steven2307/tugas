#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[2]:


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)


# In[3]:


class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
    def nthToLast(self, n):
        pointer1 = self.head
        pointer2 = self.head
        for i in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1


# In[4]:


customLL = LinkedList()
customLL.generate(10, 0, 99)


# In[5]:


print(customLL)


# In[6]:


print(customLL.nthToLast(3))

