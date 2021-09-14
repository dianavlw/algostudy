"""
344. Reverse String: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) -1
        
        while L < R:
            s[L], s[R] = s[R], s[L]
            L, R = L +1, R -1
