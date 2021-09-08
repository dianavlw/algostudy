LeetCode: Google Interview 

import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

            # Testing
-------------------------- 46. Permutations --------------------------            
"""
        46. Permutations
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
        Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
-------------------------- SOLUTION --------------------------
class Solution:
    def permute(self, nums):
        result = []
        
        if(len(nums) == 1):
            return [nums[:]] # vs copy() which will make your code slow
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms) #The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
            nums.append(n)
            
        return result

nums = [1,2,3]       
print(Solution().permute(nums)) # expected output = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]

-------------------------- Permutations --------------------------
 """
    47. Permutations II
    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
    
    Example 1:
    Input: nums = [1,1,2]
    Output:
            [[1,1,2], [1,2,1],[2,1,1]]
    Thought process:
        1,2,3
        3*2*1 n!
        
        3 permutation: list itself is one
        backtracking
        hashmap
        We have two 1's
        and we have one 2's
        num |cout
        ----------
        1     2
        _________
        2     1
        
        res = []
        perm = []
        count = { n:0 for n in nums}
        for n in nums:
            count[n] += 1
"""

-------------------------- SOLUTION --------------------------
#SOLUTION 1. 
class Solution(object):
    def permuteUnique(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[List[int]]
                
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    count[n] += 1
                    perm.pop()
                    
        dfs()
        return res


#SOLUTION 2. 
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """       
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
#SOLUTION 3. 

class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
        for x in range(len(nums)):
            #[2,3]
            #path =[1,_,_]
            self.backtrack(nums[:x] + nums[x+1], path+[nums[x]])

# SOLUTION 4. 

def permutations(word):
    if len(word) == 1:
        return [word]
    
    perms = permutations(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:1] + char + perm[i:])

    return result
print(permutations('abs'))



-------------------------- LeetCode - 15 - 3Sum-------------------------- 
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

    SOlUTION 1: https://www.youtube.com/watch?v=jzZsG8n2R9A
   TIME: O (nlogn) + o(n) =
    O(n^2)
    SPACE: o(1) or O(N) bcof the sorting
"""
#SOLUTION 1
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res
    
#SOLUTION 2: https://www.youtube.com/watch?v=8uWRUyWpy8M&t=316s
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        
        for a in range(len(nums) -1):
            if nums[a] > 0: break
            if a > 0 and nums[a] == nums[a-1]: continue
            l, r = a+1, len(nums)-1
            
            while(l < r):
                if nums[a] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[a]+ nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    output.append([nums[a], nums[l], nums[r]])
                    while l > r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l+=1
                    r-=1
        return output
    
    
-------------------------- ADD TWO NUMBERS --------------------------    
""" 2. Add Two Numbers: https://www.youtube.com/watch?v=wgFPrzTjm7s
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
""""
#SOLUTION 1. 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        #one of them could be null, set a digit to v1 to l1 only if l1 is notnull then set it to 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        # compute new digit 
        # edge case with carry 8 + 7 (our carry will be one) our loop will stop and we will 
        # forget about our carry so if our carry is not null continue
            val = v1 + v2 + carry
        # if 15 a two digit num we need to get the carry
            carry = val // 10
        # we only want the ones place
            val= val % 10 
        #insert the value into our new list node()
            cur.next = ListNode(val)
        # update our current to the next one
            cur = cur.next
        # pointers too only if theyre not null

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
       return dummy.next


#SOLUTION 2; https://www.youtube.com/watch?v=mAGn6qQTu4g&t=709s

def addTwoNumbers(self, L1, L2):
    dummy = ListNode(0)
    carry = 0
    
    while l1 or l2:
        if l1:
            l1.val = l1.val
        else:
            l1_val = 0
        if l2:
            l2.val = l2.val
        else:
            l2.val = 0
            
        sum_ = l1_val + l2.val + carry
        
        curr.next = ListNode(sum_ % 10)
        cur = cur.next
        carry = sum_ // 10 (integer division to avoid floating value)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if carry:
           curr.next = ListNode(carry)
        
        return dummy
        
-------------------------- BINARY TREE MAX SUM --------------------------
"""
Binary Tree Maximum Path Sum: https://www.youtube.com/watch?v=Hr5cWUld4vU
    
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
    1
   / \
  2   3
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
  
   -10
   / \
  9   20
      /\
    15  7
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""
#SOLUTION 1. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
  
  
  
  
-------------------------- Longest Substring Without Repeating Characters --------------------------
"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
------ SOLUTION --------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub ={}
        start = cur_length = longest = 0
        
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= start:
                start = sub[letter] + 1
                cur_length = i -sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                cur_length += 1
                if cur_length > longest:
                    longest = cur_length
        return (longest)
        
        
        """The longest substring is a string of letters that go on without repeating

Find the length of the substring
S = “abcabcbb”

Breaking it down = abc abc b b
LongestSub = abc 

Output: 3

ABC length is 3 

Iterate through the string
Set? Count each char that I find
Return the count and char 
Return a new string with new characters 
If nothing return 0

question: are there any space or special characters?
Should I add them to my solution?"""


-------------------------- Container with most Water --------------------------
"""
Container With Most Water

Solution
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
------ SOLUTION --------

class Solution:
    def maxArea(self, height: List[int]) -> int:
         res = 0
         l = 0                 
         r= len(height)-1
        
        
         while l < r:
             area = (r - l) * min(height[l], height[r])
             res = max(res, area)
            
             if height[l] < height[r]:
                 l += 1
             else:
                 r -= 1
         return res
    
        # l=0                 #initiate to left end index
        # r=len(height)-1     #initiate to right end index
        # area=0              #initial area
        # while l<r:          
        #     area1=(r-l)*min(height[l],height[r])    #calculate area of iteration
        #     area=max(area,area1)                    #save maximum area
        #     if height[l]<height[r]: 
        #         l+=1
        #     else:
        #         r-=1
        # return area
        
        
--------------------------------------- 3sum -------------------------------------------
 """       
3Sum

Solution
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5        
"""
------ SOLUTION --------


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res



--------------------------------------- Next Permutation -------------------------------------------
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
--------- SOLUTION 1 -------------
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]:
            i-=1
        i-=1
        if i<0:
            nums.reverse()
            return
        
        while j>i and nums[j]<=nums[i]:
            j-=1
        
        nums[i],nums[j] = nums[j], nums[i]
        
        k,l = i+1, len(nums)-1
        
        while k<l:
            nums[k],nums[l] = nums[l], nums[k]
            k+=1
            l-=1
            
--------- SOLUTION 2 -------------
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        pointer = length - 2
    
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        if pointer == -1:
             return nums.reverse()

        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums [x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        nums[pointer + 1:] = reversed(nums[pointer + 1:])
        


--------------------------------------- Multiply Strings  -------------------------------------------
"""

Multiply Strings
Resource: https://www.youtube.com/watch?v=1vZswirL8Y8
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""
--------------------------------------- Solution  -------------------------------------------

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
#SOLUTION 2        
        if "0" in [num1, num2]:
            return "0"
        
#         len1 = len(num1)
#         len2 = len(num2)
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10 
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        res = map(str, res[beg:])
        return "".join(res)
        
# SOLUTION 2. 
#takes more memory wont run fast
#         len1 = len(str1)
#         len2 = len(str2)
        
#         str1= list(map(int, reversed(str1)))
#         str2= list(map(int, reversed(str2)))
#         #[8,7] [7,5]
        
#         res = [0 for i in range(len1 + len2)]
#         #[0,0,0,0]
        
#         for j in range(len2):
#             for i in range(len1):
#                 res[i+j] = res[i+j] + str[i]*str[j]
#                 res[i+j+1] = res[i+j+1] + res[i+j] // 10 #carry
#                 res[i+j] = res[i+j] % 10 
                
#         return "".join(map(str,res[::-1]))




--------------------------------------- Rotate Image  -------------------------------------------
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

--------------------------------------- Solution  -------------------------------------------


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#SOLUTION 2

# reverse: https://leetcode.com/problems/rotate-image/discuss/842087/Easy-Python-from-scratch-(2-Steps)
#Transposing means: rows become columns, columns become rows.


l = 0
r = len(matrix) -1
while l < r:
	matrix[l], matrix[r] = matrix[r], matrix[l]
	l += 1
	r -= 1
# transpose 
for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
#SOLUTION 3  : https://www.youtube.com/watch?v=ymOBPRt9UR0
N = len(matrix)

for r in range(N):
  for c in range(r):
    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
for r in matrix:
    r.reverse()
OR

N = len(matrix)
matrix.reverse()
for r in range(N):
  for c in range(r):
    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    
    
--------------------------------------- Problem  -------------------------------------------

--------------------------------------- Solution  -------------------------------------------



--------------------------------------- Problem  -------------------------------------------

--------------------------------------- Solution  -------------------------------------------



--------------------------------------- Problem  -------------------------------------------

--------------------------------------- Solution  -------------------------------------------

        
