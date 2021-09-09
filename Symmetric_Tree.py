--------- Symmetric Tree  ------------
"""
Symmetric Tree: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
check these conditions:
https://www.youtube.com/watch?v=qNH6fFdb6Hs
Check if left right is not null 
root.left.left == root.right.right
root.left.right == root.right.left
          root
           1
   left 2    2(right)
      3  4  4  3
     /   |   |    \
 (R.L.L) |   |    (R.R.R)
     (R.L.R)(R.R.L)
"""
--------- SOLUTION ------------
#SOLUTION 1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)
        return leftroot == rightroot
      
#SOLUTION 2. https://www.youtube.com/watch?v=XHML8ilzESo
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      return self.mirror(root, root)
    def mirror(self, t1, t2):
      if (t1 is None and t2 is None):
        return True
      if (t1 is None or t2 is None):
        return False
      
      return (t1.val == t2.val) and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)
    
