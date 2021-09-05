# Note: put this in https://pythontutor.com
#     it will help you understand and test your code


------------------------------------ MULTIPLES OF 3 & 5 -----------------------------------------
""" https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
  
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def solution(number):
    # 3 + 5 + 6 + 9 = 23
    # multiples of 3, 5 under 10
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
                   
    
 ------------------------------------ UNIQUE IN ORDER -----------------------------------------
""" https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]   
"""
------ SOLUTION --------

def unique_in_order(iterable):
    unique_list = []
    prev = None
    
    for char in iterable:
        if char != prev:
            unique_list.append(char)
        prev = char
        
    return unique_list
        
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
  
----------------------------------------- Fill the Hard Disk Drive ----------------------------------------- 

 """
 Description:
Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.

Input:
Array of file sizes (0 <= s <= 100)
Capacity of the HD (0 <= c <= 500)
Output:
Number of files that can be fully saved in the HD.

Examples:
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12
save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, but 4+4+4 > 11

Enumerate: https://realpython.com/python-enumerate/#using-pythons-enumerate
(count, value)

Accumelator Pattern:
https://runestone.academy/runestone/books/published/thinkcspy/Strings/TheAccumulatorPatternwithStrings.html

Acuumelator Pattern in string: https://runestone.academy/runestone/books/published/thinkcspy/Strings/TheAccumulatorPatternwithStrings.html
 """
-------- SOLUTION --------
def save(sizes, hd): 
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)
  
-------- SOLUTION --------
# Note: put this in https://pythontutor.com/visualize.html#mode=display
#     it will help you understand and test your code
    
def save(sizes, hd): 
    acc = 0
    for i, item in enumerate(sizes):
        if acc + item > hd:
            return i
        acc += item
    return len(sizes)


----------------------------------------- Sum Of Digits ----------------------------------------- 
"""
https://www.codewars.com/kata/59cf805aaeb28438fe00001c/train/python

It involves implementing a program that sums the digits of a non-negative integer. 
For example, the sum of 3433 digits is 13.

Digits can be a number or a string, and you should control it is no undefined and return an empty string.
Digits can be a number or a string, and you should ensure it is not None and return an empty string.

To give you a little more excitement, the program will not only write the result of the sum, 
but also write all the sums used: 3 + 4 + 3 + 3 = 13.

('string test case)
        test.assert_equals(sum_of_digits("3433"), "3 + 4 + 3 + 3 = 13")
        test.assert_equals(sum_of_digits("64323"), "6 + 4 + 3 + 2 + 3 = 18")
        test.assert_equals(sum_of_digits("8"), "8 = 8")

(integer test case)
        test.assert_equals(sum_of_digits(3433), "3 + 4 + 3 + 3 = 13")
        test.assert_equals(sum_of_digits(64323), "6 + 4 + 3 + 2 + 3 = 18")
        test.assert_equals(sum_of_digits(8), "8 = 8")
        
(None Test Case)
(sum_of_digits(None), "")
"""


-------- SOLUTION --------
def sum_of_digits(num):
    if num is None:
        return ""
    stg = str(num)
    return f"{' + '.join(stg)} = {sum(int(d) for d in stg)}"
  
-------- SOLUTION --------

def sum_of_digits(digits):
    result = ""
    sum = 0
    for i in str(digits):
        if digits != None:
            i = int(i)
            sum += i
            result += f"{i}"
        else:
            return ""
    return " + ".join(result) + " = " + str(sum)



-----------------------------------------  ----------------------------------------- 











