"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
#SOLUTION 1.
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
"""             0, 1, 2 3 4 5 6 . .
        nums = [0,0,1,1,1,2,2,3,3,4]
                  l(not unique) so move l+=1
                  r will move and if num is unique l will replace the current one its on with it
               r-1  
               r will go to the end of the array and once its done we look at where L stands return 
               index 5 

"""

#SOLUTION 2.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
            
        
# i        
#[1,1,2]
#   j 
#nums[j] != nums[i]
# i+= 1
#   i
#[1,1,2]
        
        
# keep track of the duplicates
# traverse through the array and if its a duplicate add it to a set()

# keep track of the indecies and that value 
# when a duplicate is found replace with a _ underscore
# return the array with _
