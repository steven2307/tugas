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


# In[4]:


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result // 10

    return ll


# In[5]:


llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)


# In[6]:


print(llA)
print(llB)


# In[7]:


print(sumList(llA, llB))

