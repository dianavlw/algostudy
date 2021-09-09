
----------938. Range Sum of BST------------
"""
https://leetcode.com/problems/range-sum-of-bst/
938. Range Sum of BST
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
ex. Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
https://www.youtube.com/watch?v=ATocLyuTaKo
"""
---------SOLUTION------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s = 0
        def explore(root, low, high):
            nonlocal s
            if low<=root.val<=high:
                s += root.val
            if root.left and low<root.val:
                explore(root.left, low, high)
            if root.right and high>=root.val:
                explore(root.right, low, high)
        explore(root, low, high)
        return s
      
      
 #SOLUTION 2
   def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        sum = 0
        if root.val > L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            sum += self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            sum += root.val     
        return sum
      
  #Solution 3
  class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        if root.val==low:
            return root.val+self.rangeSumBST(root.right,low,high)
        if root.val==high:
            return root.val+self.rangeSumBST(root.left,low,high)
        return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
      
      
