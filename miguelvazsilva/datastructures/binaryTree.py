# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Binary Tree Implementation
# Copyright 2018

class BinaryTree(object):
    def __init__(self,r):
        self.root = r
        self.lefttree = None
        self.righttree= None
        
    def insertLeft(self,node):
        nd = BinaryTree(node)
        
        if (self.lefttree is None):
            self.lefttree = nd 
        else:
            nd.lefttree = self.lefttree
            self.lefttree = nd
        
    def insertRight(self,node):
        nd = BinaryTree(node)
  
        if (self.righttree is None):
            self.righttree = nd
        else:
            nd.righttree = self.lefttree
            self.righttree = nd

    def printTree(self):
        print("Root:",end='')
        print(self.root)
        
        if(self.lefttree is not None): 
            print("Left Child:",end='')
            print(self.lefttree.root)
            self.lefttree.printTree()
        else: 
            print("No Left Child")
            
        if(self.righttree is not None): 
            print("Right Child:",end='')
            print(self.righttree.root)
            self.righttree.printTree()
        else: 
            print("No Right Child")
            
    def getLeftChild(self):
        return self.lefttree 
    
    def getRightChild(self):
        return self.righttree
