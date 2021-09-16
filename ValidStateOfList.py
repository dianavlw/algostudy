"""
Valid State of List
Medium

Given a list of integers nums, return whether every number can be grouped using one of the following rules:

You can form contiguous pairs (a, a)
You can form contiguous triplets (a, a, a)
You can form contiguous triplets (a, a + 1, a + 2)
Constraints

n ≤ 100,000 where n is the length of nums.
Example 1
Input
nums = [7, 7, 3, 4, 5]
Output
True
Explanation
We can group [7, 7] together and [3, 4, 5] together.
"""
         
#SOLUTION 1. 

        firstprev, secondprev, thirdprev = False, True, False
        for i in range(1, len(nums)):
            current = False

            current |= secondprev if nums[i] == nums[i - 1] else False
            current |= thirdprev if i >= 2 and nums[i] == nums[i - 1] == nums[i - 2] else False
            current |= (thirdprev if i >= 2 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 else False)

            firstprev, secondprev, thirdprev = current, firstprev, secondprev

        return firstprev

#SOLUTION 2. 
        dp = [False] * (len(nums) + 1)
        dp[0] = True
        for i in range(2, len(nums) + 1):
            if nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True
            if i > 2:
                if nums[i - 1] == nums[i - 2] and nums[i - 2] == nums[i - 3] and dp[i - 3]:
                    dp[i] = True
                if nums[i - 1] - 1 == nums[i - 2] and nums[i - 2] - 1 == nums[i - 3] and dp[i - 3]:
                    dp[i] = True
        return dp[-1]
    
#SOLUTION 3. 
class Solution:
    def solve(self, A):
        d = deque([0])
        s = len(A)

        def a(i):
            if i >= s:
                return 1e9 + i
            return A[i]

        seen = set()

        while d:
            i = d.popleft()
            if i == s:
                return True
            if i + 2 not in seen and i + 2 <= s and a(i) == a(i + 1):
                d.append(i + 2)
                seen.add(i + 2)
            if i + 3 not in seen and i + 3 <= s and a(i) == a(i + 1) == a(i + 2):
                d.append(i + 3)
                seen.add(i + 3)
            if i + 3 not in seen and i + 3 <= s and a(i) == a(i + 1) - 1 == a(i + 2) - 2:
                d.append(i + 3)
                seen.add(i + 3)

        return False
