
--------------------------------------- Multiply Strings  -------------------------------------------
"""

Multiply Strings
Resource: https://www.youtube.com/watch?v=1vZswirL8Y8
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""
--------------------------------------- Solution  -------------------------------------------

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
#SOLUTION 2        
        if "0" in [num1, num2]:
            return "0"
        
#         len1 = len(num1)
#         len2 = len(num2)
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10 
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        res = map(str, res[beg:])
        return "".join(res)
        
# SOLUTION 2. 
#takes more memory wont run fast
#         len1 = len(str1)
#         len2 = len(str2)
        
#         str1= list(map(int, reversed(str1)))
#         str2= list(map(int, reversed(str2)))
#         #[8,7] [7,5]
        
#         res = [0 for i in range(len1 + len2)]
#         #[0,0,0,0]
        
#         for j in range(len2):
#             for i in range(len1):
#                 res[i+j] = res[i+j] + str[i]*str[j]
#                 res[i+j+1] = res[i+j+1] + res[i+j] // 10 #carry
#                 res[i+j] = res[i+j] % 10 
                
#         return "".join(map(str,res[::-1]))



