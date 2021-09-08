----------PROBLEM------------
"""
Algo Expert: Depth First Search:https://www.algoexpert.io/questions/Depth-first%20Search

"""
---------SOLUTION------------
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array



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
    
    
--------- Path Sum ------------
"""
Given the root of a binary tree and an integer targetSum, return true 
if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

    1
  /  \
 2     3
Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [1,2], targetSum = 0
Output: false

"""
--------- SOLUTION ------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
--------- 153. Find Minimum in Rotated Sorted Array ------------
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

        [3,4,5,1,2]
        L    M   R
    nums[m] >= nums[L]
          5 >= 1
* only on a rotate array
"""

--------- SOLUTION ------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
#SOLUTION 1 
        res = nums[0]
        l, r = 0, len(nums) -1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (1 + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res    
            
 
# SOLUTION 2        
#         left, right = 0, len(nums)-1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return nums[left]





--------- 33. Search in Rotated Sorted Array ------------
"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
--------- SOLUTION ------------  

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
#           [4,5,6,7,0,1,2] target = 0

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1        

#         l, r = 0, len(nums) - 1
        
#         while l <= r:
#             mid = (l + r) //2
#             if target == nums[mid]:
#                 return mid
#         #Left sorted
#         if nums[l] <= nums[mid]:
#             if target > nums[mid] and target < mid[l]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         # Right Sorted
#         else:
#             if target < nums[mid] or target > nums[r]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return -1
                
        

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
        
        
        
--------- Problem ------------
"""
"""
--------- SOLUTION ------------  

--------- Problem ------------
"""
"""
--------- SOLUTION ------------  























--------- Problem ------------
"""
"""
--------- SOLUTION ------------  







      
      
      
      
      
      
      
      
      
        
