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
