# Note: put this in https://pythontutor.com
#     it will help you understand and test your code


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
