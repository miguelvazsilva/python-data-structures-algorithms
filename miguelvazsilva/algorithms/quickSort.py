# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Quick Sort Implementation
# Copyright 2018

def qS(l):
    quickSort(l,0,len(l)-1)
    return l   
    
def quickSort(li,a,b):
    
    if a<b:
        splitpoint = partition(li,a,b)
        quickSort(li, a, splitpoint -1)
        quickSort(li,splitpoint + 1, b)
    
def partition(l,pivot,last):  
    pivotvalue = l[pivot]
    leftmark = pivot+1
    rightmark = last       
    done = False
    
    while not done:
        while(leftmark<=rightmark and l[leftmark]<=pivotvalue):
            leftmark +=1
            
        while(rightmark>=leftmark and l[rightmark]>=pivotvalue):
            rightmark -=1
                 
        if rightmark < leftmark:
            done = True
        else:
            temp = l[leftmark]
            l[leftmark] = l[rightmark]
            l[rightmark] = temp 
    
    temp = l[pivot]
    l[pivot] = l[rightmark]
    l[rightmark] = temp 
        
    return rightmark
