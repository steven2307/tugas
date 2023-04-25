#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None


# In[2]:


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def createDLL(self,nodeValue):    
        node = Node(nodeValue) 
        self.prev = None
        self.next = None
        self.head = node
        self.tail = node
        return "The DLL is created Successfully"
    
    def insertNode(self,nodeValue,location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode= Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
        
    def reverseTraverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode= self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                    
    def searchDLL(self,nodeValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode == tempNode.next
            return "The node does ot exist in this list"
    
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any element in this list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.prev = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
            
    def deleteDLL(self):
        if self.head is None:
            print("There is not any not in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")


# In[4]:


doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,1)
doubyLL.insertNode(6,2)
print([node.value for node in doubyLL])


# In[5]:


doubyLL.deleteDLL()
print([node.value for node in doubyLL])

