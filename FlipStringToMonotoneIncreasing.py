"""
video explaination that helped me:
https://www.youtube.com/watch?v=Do2BcLMfyoE


926. Flip String to Monotone Increasing 
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""

class Solution:
    def minFlipsMonoIncr(self, S): # https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/748236/Easy-Python-or-Explained-or-O(n)-time-O(1)-space
        
        cost = 0
        for x in S:
            if x=='0':
                cost += 1
        best = cost
        for x in S: 
            if x=='0':
                cost -= 1 
            else:
                cost += 1 
            best = min(best,cost)
        return best
   
  

class Solution: 
    def minFlipsMonoIncr(self, s: str) -> int: #https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/1890095/Python-simple
        
        count_one = 0
        count_zero = 0

        for i in range(len(s)):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one += 1
            # ignore leading 'zero' while counting.  Once hits 'one', count population and return the minority to get the minimum flipping needed. 
            if count_zero > count_one:
                count_zero = count_one
        
        return count_zero
      
      
      
