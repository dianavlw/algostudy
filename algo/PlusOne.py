"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

 
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""

class Solution(object):
    def plusOne(self, digits):

        digits = digits[::-1]
        one, i = 1, 0
        
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
       
#SOLUTION 2.    
#         dig_len = len(digits)
#         for i in reversed(range(dig_len)):
#             digits[i] +=1
#             if digits[i] < 10:
#                 return digits
#             else:
#                 digits[i] = 0

#         digits.insert(0,1)
#         return digits   
        
        
#SOLUTION 3:
        # if digits[-1] == 9:
        #     if len(digits) == 1:  # Already a 9
        #         return [1, 0]
        #     return self.plusOne(digits[:-1]) + [0]
        # else:
        #     digits[-1] += 1
        # return digits

