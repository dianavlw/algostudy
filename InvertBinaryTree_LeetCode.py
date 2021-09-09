
--------- 226. Invert Binary Tree ------------
"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
--------- SOLUTION ------------  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            
            node.left, node.right = node.right, node.left
        
        dfs(root) #call the root
        
        return root # return root
        
        
