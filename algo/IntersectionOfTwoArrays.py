"""

349. Intersection of Two Arrays:https://leetcode.com/problems/intersection-of-two-arrays/
Easy

Share
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

 
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
#SOLUTION 1.
class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums1:
        if i not in res and i in nums2:
            res.append(i)
    
    return res
   
#SOLUTION 2.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums1:
            d[n] = 1
          
        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1
        return res
