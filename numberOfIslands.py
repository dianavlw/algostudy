
"""
200. Number of Islands :https://leetcode.com/problems/number-of-islands/
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
O(n*m)TIME AND SPACE
we making that many calls recursively

source:https://www.youtube.com/watch?v=2Si2VWLLR9c 
https://www.youtube.com/watch?v=uDB5QXTqMn0&t=414s
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols =len(grid[0])
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1":
                    count += 1
                
                self.DFS(grid, r, c)
        return count
                
    def DFS (self, grid, r, c):
        rows = len(grid)
        col = len(grid[0])
        
        if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        
        self.DFS(grid, r+1, c)
        self.DFS(grid, r-1, c)
        self.DFS(grid, r, c+1)
        self.DFS(grid, r, c-1)
        
        
#         turn "1" = "0"
# return the sum of island
# rows, cols
# DFS
# o(n*m):time  0(1) space
# 
    
