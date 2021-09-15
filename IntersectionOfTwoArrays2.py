"""
350. Intersection of Two Arrays II: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""


# SOLUTION 1.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        final = []

        for i in nums1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in nums2:
            if i in d:
                if d[i] > 1:
                    d[i] -= 1
                else:
                    del d[i]
                final.append(i)

        return final
      
#  SOLUTION 2. 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary= {}
        array = []
        
        for n in nums1:
            if n not in dictionary:
                dictionary[n] = 1
            elif n in dictionary:
                dictionary[n] = dictionary[n] + 1
        for n in nums2:
            if n in dictionary and dictionary[n] >= 1:
                array.append(n)
                dictionary[n] = dictionary[n] - 1
                
        return array
#SOlUTION 3. 
        nums1.sort()
        nums2.sort()
        res = []
        a = 0
        b = 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                res.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        return res
