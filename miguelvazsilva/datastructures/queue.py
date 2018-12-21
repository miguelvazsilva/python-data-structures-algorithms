# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Queue Implementation
# Copyright 2018

class Queue(object):
    def __init__(self):
        self.items = []
        
    def enqueue(self,n):
        self.items.insert(0,n)
        
    def dequeue(self):
        return self.items.pop()
    
    def queuePrint(self):
        print("Queue Print:")
        for x in self.items:
            print(x) 
            
    def queueEmpty(self):
        return self.items == []
    
    def queueSize(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]
