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

              
              
              
              
    ------------------------------------ Delete A Node From The End Of The List ------------------------------------------------------              
              
Delete Matthew 
        0              1                2   
head-> John ------->  Ben --------->  Matthew -----> End of the List
        Data  Next    Data  Next      Data     Next          
                    *store in temp node
 -Traverse to the end of the list
 -store the last second node
 -delete last node
 -make the next of the temp node point to None
 
             
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
              
              
              
    def deleteEnd(self):
              john ben matthew
        lastNode = self.head
        while lastNode.next is not None:
              previousNode = lastNode
              lastNode = lastNode.next # advances to the next node but before we advance we need to store the previous node then reference it 
        previousNode.next = None
          
              
              
    def printList(self):
        currentNode = self.head
        while True:
          if currentNode is None:
            break
          print(currentNode.data)
          currentNode = currentNode.next
             
              
   
    ------------------------------------ Delete A Node ------------------------------------------------------              
      DELETE A NODE: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem        
      Delete the node at a given position in a linked list and return a reference to the head node. 
      The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.        
              
 Constraints
 1 <= n <= 1000
1 <= list[i] <= 1000 , where list[i] is the i^th element of the linked list.
Sample Input

8 (elements in the list)
20
6
2
19
7
4
15
9
3 (delete at position 3)
Sample Output

20 6 2 7 4 15 9
              
 Solution: 
 """
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

 """             

def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        llist = llist.next
    else:
        temp = llist
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
    return llist
if __name__ == '__main__':              
              
              
------------------------------------------------------------ Print in Reverse ------------------------------------------------------------------  
 Print in Reverse: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
              
 Given a pointer to the head of a singly-linked list, print each  value from the reversed list. If the given list is empty, do not print anything.          
              
  There are three test cases. There are no blank lines between test case output.

The first linked list has 5 elements: 16 -> 12-> 4 ->2 -> 5. Printing this in reverse order produces:
5
2
4
12
16

The second linked list has 3 elements: 7 ->3 -> 9 -> NULL. Printing this in reverse order produces:
9
3
7
The third linked list has 5  elements: 5 -> 1 ->18 ->3 -> 13 -> NULL. Printing this in reverse order produces:
13
3
18
1
5            
              

def reversePrint(llist):
    # Write your code here
    if llist == None:
        return
    reversePrint(llist.next)
    print(llist.data)
    
#   5 -> 1 ->18 ->3 -> 13 -> NULL
   head  head head..... NULL
              then previous step we will print the data in reverse
              
              

------------------------------------------------------------ Reverse a linked list ------------------------------------------------------------------                
Reverse a linked list: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem              
Source: https://www.youtube.com/watch?v=By2fM4vU-dU 
              
Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.              
Input Format

The first line contains an integer , the number of test cases.

Each test case has the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the  values of the elements in the linked list.     

           
Sample Input

1
5
1
2
3
4
5
Sample Output

5 4 3 2 1 
Explanation

The initial linked list is: 1 ->2 ->3-> 4-> 5-> NULL

The reversed linked list is: 5 ->4 ->3-> 2-> 1 -> NULL               
              

def reverse(llist):
    # initialize three pointers
    prev = None
    cur = llist
    next = llist.next
    
    while cur != None:
        next = cur.next 
         # change the direction of the nodes
        cur.next = prev # 1 will be poiting to null
         # shifting the nodes     
        prev = cur 
        cur = next 
    llist = prev 
    return llist 
 
              
              
 206. LeetCode Reverse Linked List             
 USING TWO POINTERS : https://www.youtube.com/watch?v=G0_I-ZF0S38
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Solution 1: 
# Time: O(n) Memory: O(n)
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
              
#  Solution 2:

        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead

             
              
 ------------------------------------------------------Compare two linked lists--------------------------------------------------------------     
 You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. 
 If all data attributes are equal and the lists are the same length, return 1 . Otherwise, return 0.
 
 https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
 https://www.youtube.com/watch?v=9mJxRgCmHe4
 
 """           
 #!/bin/python3

import os
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
"""
              
           
def compare_lists(llist1, llist2):
    head1 = llist1
    head2 = llist2

    while head1 and head2:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0
    if head1 == None and head2 == None:
        return 1
    else:
        return 0
if __name__ == '__main__':             
              
              
              
              
              
              
              
              
              
  ------------------------------------------------------Remove Nth Node From End of List--------------------------------------------------------------              
  Given the head of a linked list, remove the nth node from the end of the list and return its head.
  https://leetcode.com/problems/remove-nth-node-from-end-of-list/
              
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]          
              
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        while right: 
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        
              
              
              
              
              
              
------------------------------------------------------------ Add Two Numbers ------------------------------------------------------------------                
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.              

https://leetcode.com/problems/add-two-numbers/              
              
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.              
              
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val// 10
            val = val % 10
            
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
                          
              
              
------------------------------------------------------------ Merge two sorted linked lists ------------------------------------------------------------------                
Merge two sorted linked lists
https://programs.programmingoneonone.com/2021/05/hackerrank-merge-two-sorted-linked-lists-solution.html (this solution was cleared to me)
              
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 == None:
        return head2
    if head1 == None:
        return head2
    
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    
    current = head
    while head1 != None or head2 != None:
        if head1 == None:
            current.next = head2
            break
        if head2 == None:
            current.next = head1
            break
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    return head 
    # if head1 == None and head2 == None:
    #     return None
    # if head1 == None:
    #     return head2
    # if head2 == None:
    #     return head1
    # if head1.data < head2.data:
    #     temp = head1
    #     temp.next = mergeLists(head1.next, head2)
    # else:
    #     temp = head2
    #     temp.next = mergeLists(head1, head2.next)
    # return temp
if __name__ == '__main__':              
              
              
              
    LEET CODE: 21- MergeTwo Sorted List
    Faster time:
    class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode()
        anchor = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                anchor.next = l1
                l1 = l1.next
            else:
                anchor.next = l2
                l2 = l2.next
            anchor = anchor.next
        anchor.next = l1 if l1 else l2
        return dummy.next

    long runtime:
              
    def mergeTwoList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
              if l1.val < l2.val
                  tail.next = l1
                  l1 = l1.mext
              else:
                  tail.next = l1
              tail = tail.next
       if l1:
          tail.next = l1
       elif l2:
              tail.next = l2
       return dummy.next
              
              

              
              
              
 ------------------------------------------------------------ GET NODE VALUE ------------------------------------------------------------------                
 Given a pointer to the head of a linked list and a specific position, determine the data value at that position. 
 Count backwards from the tail node. 
 The tail is at postion 0, its parent is at 1 and so on.            
              
 Head refers to 3 -> 2 -> 1 -> NULL
 Position from Tail = 2
              
source: https://www.youtube.com/watch?v=BmkO7VEPkSo              
Logic:              
ptr =   0    1    2    3    4    5  
LList = 1 -> 3 -> 9 -> 4 -> 5  NULL
count = 5    4    3    2    1   0
              
              
              
def getNode(llist, positionFromTail):
    # Write your code here
    ptr = llist
    count = 0
    
    while ptr != None:
        count +=1
        ptr = ptr.next #moved it to the last and we now assign it the head
    ptr = llist
    count = count -1 # count from 6 -5-4- ect
    
    while ptr.next != None:
        if count == positionFromTail:
            break
        ptr = ptr.next
        count -= 1
    return ptr.data
    
    
    
    # two pointers SOLUTION
    ptr1 = llist
    ptr2 = llist
    
    #traverse to the position from the head
    for i in range(positionFromTail):
        ptr1 = ptr1.next
        
    #traverse both pointer    
    while ptr1.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
            
              
              
 -------------------------------------------------------- Delete duplicate-value nodes from a sorted linked list ---------------------------------------------------------------                
 Delete duplicate-value nodes from a sorted linked list
You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.
https://www.youtube.com/watch?v=ZfmOImyWWmk
https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem?h_r=next-challenge&h_v=zen
              
              
Example
HEAD refers to the first node in the list 1 -> 2 -> 3 -> 3 -> 3 -> 3 ->  NULL.
Remove 1 of the  data values and return  pointing to the revised list  1 -> 2 -> 3 -> NULL.             
Sample Input

STDIN   Function
-----   --------
1       t = 1
5       n = 5
1       data values = 1, 2, 2, 3, 4
2
2
3
4
Sample Output

1 2 3 4               

              
def removeDuplicates(llist):
    # Write your code here
    # creating a temporary pointer
    temp = llist
    
    while temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
            
    return llist              
              
              
 -------------------------------------------------------- Delete duplicate-value nodes from a sorted linked list ---------------------------------------------------------------                
Cycle Detection
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle.
If it does, return 1. Otherwise, return 0.

Example:
HEAD refers to the list of nodes 1 -> 2 -> 3 -> NULL

The numbers shown are the node numbers, not their data values. 
There is no cycle in this list so return .

HEAD refers to the list of nodes 1 -> 2 -> 3 -> 1 -> NULL

There is a cycle where node 3 points back to node 1, so return .
Sample Output

0
1
Explanation

The first list has no cycle, so return 0.
The second list has a cycle, so return 1.              

              
#SOLUTION 1    
              Linear time complexity bc you are storing the values
def has_cycle(head):
    res = []
    
    while head != None:
        if head not in res:
            res.append(head)
            head = head.next
        else:
            return True
    return False              
              
           
#SOLUTION 2             
slow = fast = head
              
while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next
      
      if slow == fast:
         return True
return False
              
              
              
 -------------------------------------------------------- Find Merge Point of Two Lists ---------------------------------------------------------------                
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
https://www.youtube.com/watch?v=Tttrtc9ucYY
              
Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.

Note: After the merge point, both lists will share the same node pointers.
The diagrams below are graphical representations of the lists that input nodes  and  are connected to.

Test Case 0

 1
  \
   2--->3--->NULL
  /
 1
Test Case 1

1--->2
      \
       3--->Null
      /
     1
Sample Output

2
3
Explanation

Test Case 0: As demonstrated in the diagram above, the merge node's data field contains the integer .
Test Case 1: As demonstrated in the diagram above, the merge node's data field contains the integer .            
              
              
  def findMergeNode(head1, head2):
    p1 = head1
    p2 = head2
    
    while 1:
        if p1 == p2:
            break
        p1 = p1.next
        p2 = p2.next
        if p1 == None:
            p1 = head2
        if p2 == None:
            p2 = head1
    return p1.data            
              
 LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
              
 class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1 :
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1             
---------------------------------------------------Inserting a Node Into a Sorted Doubly Linked List-----------------------------------------------------------                
Given a reference to the head of a doubly-linked list and an integer, DATA,
create a new DoublyLinkedListNode object having data value DATA and insert it at the proper location to maintain the sort.             
              
Example:
Head refers to the list 1 <-> 2 <-> 4 -> NULL              
Data = 3              
Return a reference to the new list: 1 <-> 2 <-> 3 <-> 4 -> NULL              
Sample Input:
STDIN   Function
-----   --------
1       t = 1
4       n = 4
1       node data values = 1, 3, 4, 10
3
4
10
5       data = 5
              
Sample Output:
1 3 4 5 10              
              
Explanation

The initial doubly linked list is: 1 <-> 3 <-> 5 <-> 10 -> NULL

The doubly linked list after insertion is: 1 <-> 3 <-> 4 <-> 5 <-> 10 -> NULL                  
              
              
              
              
              
              
              
              
              
              
              
              
              
