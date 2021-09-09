# Note: put this in https://pythontutor.com
#     it will help you understand and test your code

        
------------------------------------ #3 Sum of Numbers -----------------------------------------    
""" https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!  

3, 7
9, 7

n(3)

3 + 4 +5 + 6 + 7 = 25

 ** https://www.geeksforgeeks.org/range-vs-xrange-python/
 xrange() vs range():
 Memory
The variable storing the range created by range() takes more memory as compared to the variable storing the range using xrange(). 
The basic reason for this is the return type of range() is list and xrange() is xrange() object.
  
Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
""" 

-------- SOLUTION --------
def get_sum(a,b):
    if a == b:
        return a
    s = 0
    for n in range(min(a,b), max(a,b)+1):
        s += n
    return s


-------- SOLUTION --------
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
  
  
-------- SOLUTION --------
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
