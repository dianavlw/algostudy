"""
Search in a Binary Search Tree- https://leetcode.com/problems/search-in-a-binary-search-tree/
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Average: Time| O(log(n)) Space| O(log(n))
Worst: Time | O(n) Space| O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node != None:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None
