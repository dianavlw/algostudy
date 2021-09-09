
----------  POST ORDER TRAVERSAL  ------------
"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
Binary Tree Postorder Traversal:
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [3,2,1]
"""
---------SOLUTION------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
      
      
