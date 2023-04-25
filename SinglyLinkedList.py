#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# In[2]:


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode.next == None:
                        break 
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail=newNode
    
    def insertSLL(self, value, location):
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif location == -1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    if tempNode == self.tail:
                        self.tail=newNode
   
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
   
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
   
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


# In[3]:


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5,-1)

print([node.value for node in singlyLinkedList])


# In[4]:


singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList]) 


# In[12]:


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 3)
singlyLinkedList.insertSLL(7, -1)
singlyLinkedList.insertSLL(5, 6)

print([node.value for node in singlyLinkedList])

