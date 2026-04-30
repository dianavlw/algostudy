https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays
               
               
-------------------------------------------- Arrays - Left Rotation. -------------------------------------------- 
"""A left rotation operation on an array of size N shifts each of the array's elements 1 unit to the left. 
Given an integer, d, rotate the array that many steps left and return the result.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

To perform d = 4 left rotations, the array undergoes the following sequence of changes:
  [1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]

"""
def rotateLeft(d, arr):
    # Write your code here
    res = arr[0:d] # number of elements  in d
    
    for i in range(len(arr)-d):#5-d 
        arr[i] = arr[i+d] # 0-3, i = 0 , i + d
        
    arr[-d:]=res # index as minus 1, len -d to the end
    return arr
  
"""  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()  

"""
