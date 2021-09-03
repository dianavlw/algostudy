https://en.wikipedia.org/wiki/Linked_list
  
  In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. 
  Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. 
  In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence.
    This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration.
    More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions.
    A drawback of linked lists is that access time is linear (and difficult to pipeline). 
    Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.



Data Structures: Singly Linked List HEAD NODE

class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
class LinkedList:
    def __init__(self, newNode):
        self.head = None
        
    def insertEnd(self, newNode):     
        if self.head == None:
          self.head = newNode
        else:
          lastNode = self.head
          while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
            lastNode.next = newNode       
          
    def printList(self):
        currentNode = self.head
        while True:
          if currentNode is None:
            break
          print(currentNode.data)
          currentNode = currentNode.next


firstNode = Node("Amy")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)

secondNode = Node("Ben")
linkedList.iinsertEnd(secondNode)

thirdNode = Node("Donut")
LinkedList.insertEnd(thirdNode)

linkeList.printList()


 ------------------------------------ PRINT NODES ------------------------------------------------------     

Print the Elements of a Linked List   
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem   

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

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next
    

if __name__ == '__main__':    

  

 ------------------------------------ INSERT NEW NODE AT THE TAIL OF THE LIST  ------------------------------------------------------     
  
  
Insert a Node at the Tail of a Linked List:

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
    

if __name__ == '__main__':
    
 
 ------------------------------------ INSERT NEW NODE HEAD OF THE LIST ------------------------------------------------------        
    
Insert a node at the head of a linked list

Given a pointer to the head of a linked list, insert a new node before the head. 
The  value in the new node should point to  and the  value should be replaced with a given value. 
Return a reference to the new head of the list. 
  The head pointer given may be null meaning that the initial list is empty.

Function Description

Complete the function insertNodeAtHead in the editor below.

insertNodeAtHead has the following parameter(s):

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
def insertNodeAtHead(llist, data):
    #Create new node
    node = SinglyLinkedListNode(data)
    
    if llist != None:
        node.next = llist
    return node
    
    

if __name__ == '__main__':    
    
    

 ------------------------------------ INSERT NEW NODE ------------------------------------------------------     
    
Insert a New Node As The Head Node: https://www.youtube.com/watch?v=nH_nhfEZ7hc&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=4
Insert "Matthey"

head-> John  ---->  Ben
       Data  Next 
Store John in a temporary node we can remove John and make Matthew, then Matthew can point to John and John to Ben  
Head ----> Matthew ----> John ----> Ben
- Preserve the current head node in a temp node , ake a new node as the head node, make the next of your new node point to the temporary node

From Previous :
  
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
class LinkedList:
    def __init__(self, newNode):
        self.head = None
    
    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temproraryNode
        del temporaryNode
    
    def insertEnd(self, newNode):     
        if self.head == None:
          self.head = newNode
        else:
          lastNode = self.head
          while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
            lastNode.next = newNode       
          
    def printList(self):
        currentNode = self.head
        while True:
          if currentNode is None:
            break
          print(currentNode.data)
          currentNode = currentNode.next

 ------------------------------------ INSERT NEW NODE Between TWO NODES ------------------------------------------------------         
Insert A New Node In Between Two Nodes
Insert 15

head-> 10 ------->  20
      Data  Next 
Store in temporary node before advancing to the next node
remove connection from 10 to 20 and connect 10 to 15

new:
  head-> 10 ------->15-->20
      Data   Next 
-traverse the list till position 1, store the detaisl of previous node
-make a connection form the next of previous node to the new node
-ake connection from next of new node to node at position 1
source: https://www.youtube.com/watch?v=Z0uqXuzCQTo&list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&index=6



From Previous :
  
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
class LinkedList:
    def __init__(self, newNode):
        self.head = None
    
    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temproraryNode
        del temporaryNode
        
        
    def ListLength(self): # traverse the first node to the last and count the node returning the count
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
      
    #inserting position as 1, we want to insert to that location)
    # head -->10-->20--> None || newNode-->15-->None || position--> 1
    def insertAt(self, newNode, position):
      if position < 0 or position > self.listLength(): #
        print("invalid position)
      if position 0: # if position is 0 then insert at the head
         self.insertHead(newNode)
          return
        currentNode = self.head
        currentPosition = 0
        while True: # current node was 10 but before we advance we store the previous node
          if currentPosition == position:
            previousNode.next = newNode # 10
            newNode.next = currentNode # 20
            break
          previousNode = currentNode #storing the 10 
          currentNode = currentNode.next # advancing the node to the next one
          currentPosition += 1 # advancind the position down 
      
      
    def insertEnd(self, newNode):     
        if self.head == None:
          self.head = newNode
        else:
          lastNode = self.head
          while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
            lastNode.next = newNode       
          
    def printList(self):
        currentNode = self.head
        while True:
          if currentNode is None:
            break
          print(currentNode.data)
          currentNode = currentNode.next
