#88. Merge Sorted Array
#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1."""

 """
        Do not return anything, modify nums1 in-place instead.
        """
        # create a LAST variable to insert the values 
        # LAST variable will consist of m + n
        #while we have m, n values > 0
        # compare nums1 and nums 2 and place in LAST 
        # decrement both m and n 
            """
                                L
            nums1 = [1,2,3,0,0,0]
            m = 3

            nums2=[2, 5, 6]
            n = 3
            """
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        last = m + n -1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1 
            else:
                nums1[last] = nums2[n-1]
                n -=1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1



"""
#credit to CodingNinga : https://www.youtube.com/watch?v=TTWKBqG-6IU&t=1s

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
"""
