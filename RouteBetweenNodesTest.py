#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = []
        queue = [startNode]
        path = []
        
        while queue:
            deVertex = queue.pop(0)
            path.append(deVertex)
            if deVertex == endNode:
                return path
            if deVertex not in visited:
                visited.append(deVertex)
                queue.extend(self.gdict[deVertex])
        
        return None

customDict = {
    "a": ["c", "d", "b"],
    "b": ["j"],
    "c": ["g"],
    "d": [],
    "e": ["f", "a"],
    "f": ["i"],
    "g": ["d", "h"],
    "h": [],
    "i": [],
    "j": []
}

g = Graph(customDict)
print(g.checkRoute("a", "j"))

