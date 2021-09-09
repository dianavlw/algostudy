
----------Preorder Traversal:------------
"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
Binary Tree Preorder Traversal:
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [1,2,3]
"""
----------SOLUTION------------
      

  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Recursive:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return[root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
  
#iterative:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack != []
          root = stack.pop()
          result.append(root.val)
          if root.right is not None:
            stack.append(root.right)
          if root.left is not None:
            stack.append(root.left)
       return result
