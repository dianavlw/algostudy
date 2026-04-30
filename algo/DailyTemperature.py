"""
739. Daily Temperatures : https://www.youtube.com/watch?v=cTBiBSnjO3c

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#SOLUTION 1. 
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: #find the higher
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res

        
        
        
#SOLUTION 2.         
#         res = [0] * len(temperatures)
#         #[0,0,0,0,0,0,0,..]
        
#         stack = [] #pair: [temp, index]
        
#         for i, t in enumerate(temperatures):
#             while stack and t > stack[-1][0]: #is our stack empty is it greater or top idex[-1] 1st pari [0]
#                 stackT, stackInd = stack.pop()
#                 res[stackInd] = (i - stackInd)
#             stack.append([t, i])
#         return res
        
