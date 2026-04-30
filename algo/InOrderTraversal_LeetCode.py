
--------- Inorder Traversal------------
"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
Binary Tree : Inorder Traversal: 
Input: root = [1,null,2,3]
Output: [1,3,2]
"""
--------- IN ORDER TRAVERSAL ------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
