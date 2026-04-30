
-------------------------- LeetCode - 15 - 3Sum-------------------------- 
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
    
