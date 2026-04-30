

--------------------------------------- Rotate Image  -------------------------------------------
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

--------------------------------------- Solution  -------------------------------------------


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#SOLUTION 2

# reverse: https://leetcode.com/problems/rotate-image/discuss/842087/Easy-Python-from-scratch-(2-Steps)
#Transposing means: rows become columns, columns become rows.


l = 0
r = len(matrix) -1
while l < r:
	matrix[l], matrix[r] = matrix[r], matrix[l]
	l += 1
	r -= 1
# transpose 
for i in range(len(matrix)):
	for j in range(i):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
#SOLUTION 3  : https://www.youtube.com/watch?v=ymOBPRt9UR0
N = len(matrix)

for r in range(N):
  for c in range(r):
    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
for r in matrix:
    r.reverse()
OR

N = len(matrix)
matrix.reverse()
for r in range(N):
  for c in range(r):
    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    
