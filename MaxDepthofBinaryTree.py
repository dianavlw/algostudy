
--------- Maximum Depth of Binary Tree ------------
"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
---------SOLUTION------------
  

"""
Reading:   Solve Tree Problems Recursively
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/
"""
#https://www.youtube.com/watch?v=hTM3phVI6YQ
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#ITERATIVE BFS: QUEUE

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level 
      
#ITERATIVE DFS: CALL STACK          
class Solution: 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        res = 1
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res        
      
#SOLUTION 2 : RECURSIVELY 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
      
