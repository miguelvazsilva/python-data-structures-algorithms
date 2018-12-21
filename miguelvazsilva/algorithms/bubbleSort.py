# Miguel Vaz Silva
# Data Structures and Algorithms in Python - Bubble Sort Implementation
# Copyright 2018

def bubblesort(l):
    s = len(l)
    i=0
    swap = 0
    
    while (i<s-1):
        if(l[i]>l[i+1]):
            temp = l[i]
            l[i] = l[i+1]        
            l[i+1] = temp
            swap+=1
        i+=1
        
    if(swap>0):
        l=bubblesort(l)
    return l
