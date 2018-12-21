# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Ordered Linked List Implementation
# Copyright 2018

class OrderedLinkedList(object):
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def findNode(self,d):
        root = self.getRoot()
        
        while(root is not None):
            if(root.data == d):
                return True
            root = root.getnext()    
        return False
    
    def addNodeSort(self,d):
        root = self.getRoot()
        oldNode = None
                        
        if(root is None):
            #Blank Root
            nd = Node(d)
            self.root = nd
            self.size += 1
         
        else:   
           
            if(d < root.data):    
                #New Root
                nd = Node(d)
                nd.setNext(self.root)
                self.root = nd
                self.size += 1
            
            else:
                
                while(root is not None):
                    if(d < root.data):  
                        #Lower Item   
                        nd = Node(d)   
                        nd.setNext(oldNode.next)
                        oldNode.setNext(nd)
                        self.size += 1
                        break
                    oldNode = root  
                    root = root.getNext()
                
                if(root is None):
                    #Last Item
                    nd = Node(d)
                    oldNode.setNext(nd)
                    self.size += 1  


    def removeNode(self,d):
        thisNode = self.getRoot()
        prevNode = None
        
        while(thisNode is not None):
            if(thisNode.data == d and prevNode is not None):
                prevNode.setNext(thisNode.getNext())
            if(thisNode.data == d and prevNode is None):
                self.root.setnext(thisNode.getnext())
            prevNode = thisNode
            thisNode = thisNode.getNext()    
    
    def getSize(self):
        return self.size
    
    def getRoot(self):
        return self.root
    
    def listOrderedLinkedList(self):
        
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
