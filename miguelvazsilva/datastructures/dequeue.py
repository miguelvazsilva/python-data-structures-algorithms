# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Dequeue Implementation
# Copyright 2018

class Dequeue(object):
    def __init__(self):
        self.items = []
        
    def addFront(self,n):
        self.items.insert(0,n)
        
    def addBack(self,n):
        self.items.append(n)
        
    def removeBack(self):
        return self.items.pop()
    
    def removeFront(self):
        return self.items.pop(0)
    
    def dequeuePrint(self):
        print("Queue Print:")
        for x in self.items:
            print(x) 
            
    def dequeueEmpty(self):
        return self.items == []
    
    def dequeueSize(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]
