"""
1413 Mininum Value to get Positive step by step sum
"""

class Solution:
    def minStartValue(nums):
        runningSum = 0
        minSum = 0

        for num in nums:
            runningSum += num
            minSum = min(minSum, runningSum)
        return -minSum + 1 if minSum < 1 else 1


class Solution:
    def minStartValue(nums):
        minval = 0
        total = 0

        for num in nums:
            total += num
            minval = min(minval, total)
        return -minval + 1

        