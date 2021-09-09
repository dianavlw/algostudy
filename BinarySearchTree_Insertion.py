"""
LeetCode: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

You are given a pointer to the root of a binary search tree and values to be inserted into the tree. 
Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. 
You just have to complete the function.

"""

------------- SOLUTION ---------------

# class Node:
#     def __init__(self, info):
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     def __str__(self):
#         return str(self.info) 

# def preOrder(root):
#     if root == None:
#         return
#     print (root.info, end=" ")
#     preOrder(root.left)
#     preOrder(root.right)
    
# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

# #Node is defined as
# #self.left (the left child of the node)
# #self.right (the right child of the node)
# #self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        newnode = Node(val)
        
        if self.root is None:
            self.root = newnode
            return 
        
        curr = self.root
        while curr:
            if val < curr.info:
                if curr.left is None:
                    curr.left = newnode
                    return 
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = newnode
                    return
                curr = curr.right      
        










