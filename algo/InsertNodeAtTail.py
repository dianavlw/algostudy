   
""" Insert a Node at the Tail of a Linked List:

https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

Function Description

Complete the insertNodeAtTail function in the editor below.

insertNodeAtTail has the following parameters:

SinglyLinkedListNode pointer head: a reference to the head of a list
int data: the data value for the node to insert
Returns

SinglyLinkedListNode pointer: reference to the head of the modified linked list
Input Format

The first line contains an integer , the number of elements in the linked list.
The next  lines contain an integer each, the value that needs to be inserted at tail.

Constraints

Sample Input

STDIN Function ----- -------- 5 size of linked list n = 5 141 linked list data values 141..474 302 164 530 474

Sample Output

141
302
164
530
474

#!/bin/python3



class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

"""
------------- SOLUTION------------
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    #head pointer is null
    if head == None:
        head = node
    else:
        #insert node at tail
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        
    return head
    

# if __name__ == '__main__':
    
    
