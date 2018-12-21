# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Stack Implementation
# Copyright 2018

class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self,n):
        self.items.insert(0,n)
        
    def pop(self):
        return self.items.pop(0)
    
    def stackPrint(self):
        print("Stack Print:")
        for x in self.items:
            print(x) 
            
    def stackEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
