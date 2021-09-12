"""
Rotate Array:
Given an array, rotate the array to the right by k steps, where k is non-negative.
https://leetcode.com/problems/rotate-array/
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
https://www.youtube.com/watch?v=gmu0RA5_zxs
https://www.youtube.com/watch?v=8kyZPizZzWc

Let n = 7n=7 and k = 3k=3.

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
Complexity Analysis

Time complexity: \mathcal{O}(n)O(n). nn elements are reversed a total of three times.

Space complexity: \mathcal{O}(1)O(1). No extra space is used.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#  SOLUTION 1. 
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        
#  SOLUTION 2.        
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
# SOLUTION 3. 
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        
