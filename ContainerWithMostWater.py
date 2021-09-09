


-------------------------- Container with most Water --------------------------
"""
Container With Most Water : https://leetcode.com/problems/container-with-most-water/

Solution
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
------ SOLUTION --------

class Solution:
    def maxArea(self, height: List[int]) -> int:
         res = 0
         l = 0                 
         r= len(height)-1
        
        
         while l < r:
             area = (r - l) * min(height[l], height[r])
             res = max(res, area)
            
             if height[l] < height[r]:
                 l += 1
             else:
                 r -= 1
         return res
    
        # l=0                 #initiate to left end index
        # r=len(height)-1     #initiate to right end index
        # area=0              #initial area
        # while l<r:          
        #     area1=(r-l)*min(height[l],height[r])    #calculate area of iteration
        #     area=max(area,area1)                    #save maximum area
        #     if height[l]<height[r]: 
        #         l+=1
        #     else:
        #         r-=1
        # return area
