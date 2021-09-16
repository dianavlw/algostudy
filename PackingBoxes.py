"""
Packing Boxes - https://binarysearch.com/problems/Packing-Boxes
Medium

Given a list of integers nums, pack consecutive elements of the same value into sublists.

Note: If there's only one occurrence in the list it should still be in its own sublist.

Constraints

0 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [4, 4, 1, 6, 6, 6, 1, 1, 1, 1]
Output
[
    [4, 4],
    [1],
    [6, 6, 6],
    [1, 1, 1, 1]
]
"""

# Store index of the start of the consecutive numbers. 
#If you find a new number just slice the array from current index - 1 to start index of the consecutive number .
class Solution:
    def solve(self, nums):
        if not nums:
            return nums
        res = [[nums[0]]]
        for i in nums[1:]:
            if i == res[-1][-1]:
                res[-1].append(i)
            else:
                res.append([i])
        return res


#take the last sublist appended and add i to that sublist
class Solution:
    def solve(self, nums):
        items = []
        item = ""
        for i in nums:
            if i == item:
                items[-1].append(i)

            else:
                item = i
                items.append([])
                items[-1].append(i)
        return items
        
        
class Solution:
    def solve(self, nums):
        answer = []
        n = len(nums)
        for i in range(n):
            if not answer:
                answer.append([])
                answer[-1].append(nums[i])
                continue
            if nums[i] == answer[-1][0]:
                answer[-1].append(nums[i])
            else:
                answer.append([])
                answer[-1].append(nums[i])
        return answer
