
---------- LEVEL ORDER TRAVERSAL  ------------
"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/990/
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
102. Binary Tree Level Order Traversal
Binary Tree Level Order Traversal: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
---------SOLUTION------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue_ = [root]
        next_queue = []
        level = []
        result = []
        while queue_ != []:
            for root in queue_:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue_ = next_queue 
            next_queue = []
        return result 
        
        


https://www.youtube.com/watch?v=MBZ-gBkjdMc
