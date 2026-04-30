
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
                
