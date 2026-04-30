"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/solution/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        for i in nums:
            if i not in set:
                set[i] = 1
            else:
                return True
        return False
                
