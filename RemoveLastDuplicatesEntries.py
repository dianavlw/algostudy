"""
Remove Last Duplicate Entries : https://binarysearch.com/problems/Remove-Last-Duplicate-Entries
Given a list of integers nums, find all duplicate numbers and delete their last occurrences.
Constraints:
0 ≤ n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [1, 3, 4, 1, 3, 5]
Output
[1, 3, 4, 5]

Example 2
Input
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
Output
[1, 1, 2, 2, 3, 3]
"""

Time Complexity
\mathcal{O}(n)O(n) We go through the array twice each of which is N elements

Space Complexity
\mathcal{O}(n)O(n) We use three auxiliary data structures, each having N elements

class Solution:
    def solve(self, nums):
        res = []
        first = {}
        last = {}

        for idx, num in enumerate(nums):
            if num not in first:
                first[num] = idx
            last[num] = idx

        for idx, num in enumerate(nums):
            if first[num] == last[num]:
                res.append(num)
                continue
            if last[num] != idx:
                res.append(num)
        return res
      
#SOLUTION 2. 
Time Complexity
\mathcal{O}(n)O(n). Because we look thru the digits once. I would appreciate if anybody bothered correcting me if this is wrong.

Space Complexity
\mathcal{O}(n)O(n) I'm kinda new so it would be nice if you corrected me.

class Solution:
    def solve(self, nums):
        cont = Counter(nums)
        se = set()

        for ind in reversed(range(len(nums))):

            if cont[nums[ind]] != 1 and nums[ind] not in se:
                se.add(nums[ind])
                nums.pop(ind)

        return nums

#SOLUTION 3. 

Implementation
c = Counter(nums) implements step 1 given above.
Step 2 is implemented by the for loop.

Time Complexity
\mathcal{O}(n)O(n) for making the frequency counter and then a single pass over nums

Space Complexity
\mathcal{O}(n)O(n) for both the counter and the result

class Solution:
    def solve(self, nums):
        c = Counter(nums)
        res = []
        for val in nums:
            if c[val] == 0:
                continue
            res.append(val)
            c[val] -= 1
            if c[val] == 1:
                c[val] = 0

        return res
