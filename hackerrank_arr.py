https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays
  
-------------------------------------------- Arrays - DS. -------------------------------------------- 
def reverseArray(a):
    # Write your code here
    return a[::-1]

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
               
               
               
               
-------------------------------------------- Arrays - Left Rotation. -------------------------------------------- 
A left rotation operation on an array of size N shifts each of the array's elements 1 unit to the left. 
Given an integer, d, rotate the array that many steps left and return the result.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

To perform d = 4 left rotations, the array undergoes the following sequence of changes:
  [1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]


def rotateLeft(d, arr):
    # Write your code here
    res = arr[0:d] # number of elements  in d
    
    for i in range(len(arr)-d):#5-d 
        arr[i] = arr[i+d] # 0-3, i = 0 , i + d
        
    arr[-d:]=res # index as minus 1, len -d to the end
    return arr
  
  
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



-------------------------------------------- Arrays - Sparse Arrays. --------------------------------------------

There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.

def matchingStrings(strings, queries):
    # Write your code here
    res = []
    
    for i in range(len(queries)):
        counter = 0
        for j in range(len(strings)):
            if queries[i]==strings[j]:
                counter+= 1
        res.append(counter)
    return res 




Problem Solving:https://www.hackerrank.com/domains/algorithms

----------------------------------------------- Reapeated String ------------------------------------------------
""" Source: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

There is a string, s , of lowercase English letters that is repeated infinitely many times. 
Given an integer, n , find and print the number of letter a's in the first n letters of the infinite string.

Sample Input 0

aba
10
Sample Output 0

7
"""

------------------------------------------------ SOLUTION --------------------------------------------------------------

    def repeatedString(s, n):
    # SOLUTION 1: https://www.youtube.com/watch?v=v4v2GLHivx0&list=PLe_c5cyDuuSDl7VcoDzpC_tRbADQ1xs9T&index=32&t=617s
    l = len(s)
    
    res = (s.count('a') * (n//l)) + s[:n%l].count('a')
    
    return res
    # len_rep = n // l
    # rem = s[:n%l]
    # rep_str =  ((s * len_rep) +rem)
    # count_a = rep_str.count('a')
    # return count_a

    # SOLUTION 2: https://www.youtube.com/watch?v=XWG58qrcB50&t=478s
    l = len(s)
    rep_str = (n//l)
    
    a_count = s.count('a')
    x1= a_count * rep_str  
    x2 = s[:n%l].count('a')
    
    return x1 +x2

    #SOLUTION 3:https://www.youtube.com/watch?v=-PbKDdyo3VY
    total = 0
    for i in s:
        if i == "a":
            total += 1
    
    total = n//len(s) * total
    l = len(s)
    for i in s[:n%l]:
        if i == 'a':
            total += 1
    
    return total     
    
    
    
    """
    s = aba
    n = 10
    char_sum = 0
    for char in s:
        char += s[char]
        char_sum += 1
        if char <= len(n):
            return char_sum
     
    """
    

----------------------------------------------- Arrays: Left Rotation ------------------------------------------------    
    
"""
HACKERRANK: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d , perform d left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.
"""

------------------------------------------------ SOLUTION --------------------------------------------------------------
#Solution 1:
def rotLeft(a, d):
    # Write your code here
    return a[d:] + a[:d]

#Solution 2:
def rotLeft(a, d):
    # Write your code here
    
    return a[(n+d)%n:] + a[0:(n+d)%n] 


----------------------------------------------- PROBLEM ------------------------------------------------
""""
HACKERRANK:
Source:
""""
------------------------------------------------ SOLUTION --------------------------------------------------------------







