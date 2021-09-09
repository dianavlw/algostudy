"""
HackerRank:
Insert a node at the head of a linked list

Given a pointer to the head of a linked list, insert a new node before the head. 
The  value in the new node should point to  and the  value should be replaced with a given value. 
Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.

SinglyLinkedListNode llist: a reference to the head of a list
data: the value to insert in the  field of the new node
Input Format

The first line contains an integer , the number of elements to be inserted at the head of the list.
The next  lines contain an integer each, the elements to be inserted, one per function call.

Constraints

Sample Input

5
383
484
392
975
321
Sample Output

321
975
392
484
383    
    
    
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

""" 
------------------ SOLUTION ---------------------
def insertNodeAtHead(llist, data):
    #Create new node
    node = SinglyLinkedListNode(data)
    
    if llist != None:
        node.next = llist
    return node
    
    

# if __name__ == '__main__':    
    
