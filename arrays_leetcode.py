LeetCode: Google Interview 

Covering in this file:
  Longest Substring Without Repeating Characters
  Container with most Water
  3Sum
  Next Permutation 
  Multiply Strings
  Rotate Image
  
  
  
  
-------------------------- Longest Substring Without Repeating Characters --------------------------
"""
Solution
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








        
