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


# In[6]:


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


# In[7]:


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode

def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


# In[8]:


llA = LinkedList()
llA.generate(3,0, 10)

llB = LinkedList()
llB.generate(4,0, 10)


# In[9]:


addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)


# In[10]:


print(llA)
print(llB)


# In[11]:


print(intersection(llA, llB))

