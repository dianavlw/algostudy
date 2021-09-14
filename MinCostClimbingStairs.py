"""
746. Min Cost Climbing Stairs: https://leetcode.com/problems/min-cost-climbing-stairs/
https://leetcode.com/problems/min-cost-climbing-stairs/discuss/657490/Python-solution-from-a-beginner-(some-easy-steps-to-follow-to-solve-dp)
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
-----------------
Getting the min of both indx and adding that min to the next one

ex. [1,100,1,1,1,100,1,1,100,1]
min= 1,100
      1+1=2,
min= 100,2= 
        2 +1=3,
so far its looking like this:
[1,100, 2, 3...] we keep doing until we ended up with 6 our min cost output is 6
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        
        if len(cost) >=2:
            dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
        return min(dp[-1], dp[-2])
        
        """
        
        [0] [1] [2]
        n-1 n-2
min()=    res + n+1
return min()

        
        """
        
