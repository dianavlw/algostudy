
-------------------------- ADD TWO NUMBERS --------------------------    
""" 2. Add Two Numbers: https://www.youtube.com/watch?v=wgFPrzTjm7s
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
""""
#SOLUTION 1. 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        #one of them could be null, set a digit to v1 to l1 only if l1 is notnull then set it to 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        # compute new digit 
        # edge case with carry 8 + 7 (our carry will be one) our loop will stop and we will 
        # forget about our carry so if our carry is not null continue
            val = v1 + v2 + carry
        # if 15 a two digit num we need to get the carry
            carry = val // 10
        # we only want the ones place
            val= val % 10 
        #insert the value into our new list node()
            cur.next = ListNode(val)
        # update our current to the next one
            cur = cur.next
        # pointers too only if theyre not null

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
       return dummy.next


#SOLUTION 2; https://www.youtube.com/watch?v=mAGn6qQTu4g&t=709s

def addTwoNumbers(self, L1, L2):
    dummy = ListNode(0)
    carry = 0
    
    while l1 or l2:
        if l1:
            l1.val = l1.val
        else:
            l1_val = 0
        if l2:
            l2.val = l2.val
        else:
            l2.val = 0
            
        sum_ = l1_val + l2.val + carry
        
        curr.next = ListNode(sum_ % 10)
        cur = cur.next
        carry = sum_ // 10 (integer division to avoid floating value)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if carry:
           curr.next = ListNode(carry)
        
        return dummy
