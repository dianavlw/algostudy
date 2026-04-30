-------------------------- 46. Permutations --------------------------            
"""
  LeetCode
  46. Permutations
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
        Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
-------------------------- SOLUTION --------------------------
class Solution:
    def permute(self, nums):
        result = []
        
        if(len(nums) == 1):
            return [nums[:]] # vs copy() which will make your code slow
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms) #The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
            nums.append(n)
            
        return result

nums = [1,2,3]       
print(Solution().permute(nums)) # expected output = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
