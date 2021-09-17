"""
814. Binary Tree Pruning: https://leetcode.com/problems/binary-tree-pruning/

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

 
Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return root
        root.left = self.pruneTree(root.left)  # Set new root.left
        root.right = self.pruneTree(root.right)  # Set new root.right
        if root.left != None or root.right != None or root.val == 1:  # Check if current subtree contain 1 or not?
            return root
        return None  # If not, return None
# Complexity

# Time: O(N), where N is the number of nodes in the Binary Tree.
# Space: O(H), where H is the height of the Binary Tree, it's the cost of depth recursion stack.
