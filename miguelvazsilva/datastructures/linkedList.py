# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Linked List Implementation
# Copyright 2018

class LinkedList(object):
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def findNode(self,d):
        root = self.getRoot()
        
        while(root is not None):
            if(root.data == d):
                return True
            root = root.getNext()    
        return False
    
    def addNode(self,d):
        node1 = Node(d);
        oldRoot = self.root
        self.root = node1
        self.size +=1
        self.root.setNext(oldRoot)

    def removeNode(self,d):
        thisNode = self.getRoot()
        prevNode = None
        
        while(thisNode is not None):
            if(thisNode.data == d and prevNode is not None):
                prevNode.setNext(thisNode.getNext())
            if(thisNode.data == d and prevNode is None):
                self.root.setNext(thisNode.getNext())
            prevNode = thisNode
            thisNode = thisNode.getNext()    
    
    def getSize(self):
        return self.size
    
    def getRoot(self):
        return self.root
    
    def listLinkedList(self):
        
        root = self.getRoot()
    
        print("Root:",end='')
        print(root.printData())
        print("Next:",end='')
        print(root.printNext().data)
        
        node1 = root.getNext()
        
        while node1 is not None:
            
            print("Node:",end='')
            print(node1.data)
            if(node1.next != None and node1.next.data != None):
                print("Next:",end='')
                print(node1.printNext().data)
            else:
                print("Next:",end='')
                print(node1.printNext())        
            node2 = node1.getNext()
            node1 = node2
        
class Node(object):

    def __init__(self, d, n = None):
        self.data = d
        self.next = n
    
    def getNext(self):
        return self.next
        
    def setNext(self,n):
        self.next = n
        
    def printData(self):
        return self.data
        
    def printNext(self):
        return self.next
