#!/usr/bin/env python
# coding: utf-8

# In[1]:


class  Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = ()
        self.gdict = gdict
        
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
                    
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                        visited.append(adjacentVertex)
                        stack.append(adjacentVertex)


# In[2]:


customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }


# In[3]:


g = Graph(customDict)


# In[4]:


g.dfs("a")

