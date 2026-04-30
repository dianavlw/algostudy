"""
8. String to Integer (atoi) (READ ALL ITS ALL IMP for your CODE)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

class Solution:
    def myAtoi(self, s: str) -> int:

        integer = ''
        
        for i in range(len(s)):
            if s[i] != ' ' and s[i] != '+' and s[i] != '-' and not s[i].isdigit():
                return 0
            if s[i] == '+' or s[i] == '-' or s[i].isdigit():
                integer += s[i]
                #we want to add every num after, we want to interate until we get a char that is not a num
                j = i+1
                while j < len(s) and s[j].isdigit():
                    integer += s[j]
                    j += 1
                break
        
        if not integer or integer == '+' or integer == '-': 
            return 0
       
        integer = int(integer)
        
        if integer > 2**31-1:
            return 2**31-1
        
        elif integer < -2**31:
            return -2**31
        else:
            return integer

        """
white space: .strip()
if s[0] == "-" / "+"
.isnumeric()
out of range= conver str to int
ord(1) 49
ord(0) 48
ord(1) - ord(0) = 1

"10"
ord(10) - ord(0)= 58-48 = 10



-2**31<s<2**31
        else return -2**31 if sign is "-" else sign is "+" return 2**31
        
        if char[i] == "alphabeth" return 0
        
        if " " continue
        
        first non-whitespace character has to either = '+' or '-' or int
        """
#         returning integer 
        
