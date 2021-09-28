"""
270. Closest Binary Search Tree Value : https://leetcode.com/problems/closest-binary-search-tree-value/
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        #SOLUTION 1:
            def closestValue(self, root, target):
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r
    
    
    #SOLUTION 2:
        self.closest = float('inf')
        
        def helper(root, value):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val
                
            # Target should be located on left subtree
            if target < root.val:
                helper(root.left, target)
                
            # target should be located on right subtree
            if target > root.val:
                helper(root.right, target)
        
        helper(root, target)
        return self.closest
	# SOLUTION 3:
        minVal = 0
        minDiff = float('inf')
        while root is not None:
            if minDiff > abs(target - root.val):
                minDiff = abs(target - root.val)
                minVal = root.val
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            elif target < root.val:
                root = root.left
            else:
                root = root.right

        return minVal
