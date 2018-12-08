#!/bin/python3
import math
import os
import random
import re
import sys

# Hackerrank 
# https://www.hackerrank.com/challenges/jumping-on-the-clouds


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # insert in front of list 
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
            

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0 
    l = LinkedList()
    # insert clouds into LinkedList
    for cloud in c:
        l.insert(cloud)

    ptr = l.head

    for i in range(len(c)):
        if (ptr.next == None):
            return steps
        if ptr.next.data == 0 and ptr.next.next == None:            
            ptr = ptr.next
            steps += 1
            print("next case: " + str(steps))
        elif ptr.next.data == 0 and ptr.next.next.data == 0:          
            ptr = ptr.next.next
            steps += 1 
            print("nextnext case: " + str(steps))
        elif ptr.next.data == 0:            
            ptr = ptr.next
            steps += 1
            print("next case: " + str(steps))        
        elif ptr.next.data == 1:            
            ptr = ptr.next.next
            steps += 1
            print("1 case: " + str(steps))
    return steps
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
