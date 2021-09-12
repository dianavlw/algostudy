"""
Reverse String: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
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
