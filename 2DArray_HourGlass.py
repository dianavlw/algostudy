"""
https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays
  
-------------------------------------------- 2D Array - Hourglass -------------------------------------------- 
https://www.hackerrank.com/challenges/2d-array/problem
  Read Constraints:
    note: This means that the smallest possible value will be -9*7 (as there are 7 elements in an hourglass)
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
"""
# https://www.youtube.com/watch?v=J1aQ9JN4vZY
def hourglassSum(arr):
    # Write your code here
    maxsum = -99
    
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            hourglass = top + mid + bottom
            
            maxsum = max(hourglass, maxsum)
    return maxsum
# SOLUTION 2.   
  def hourglassSum(arr):
    max =float('inf)
    
    for i in range(1,5):
        for j in range(1,5):
               sum =0 #taking the sum of evey indiv not total, max sum vs max of the hourglass
               sum +=arr[i][j]
               sum+= arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] #a+b+c
               sum+= arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]# bottom row
               
               if sum > max:
                  max = sum
   retrun max

               
