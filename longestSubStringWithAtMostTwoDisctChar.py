"""
159. Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = end = max_len = 0
        d = {}
        
        while end < len(s):
            d[s[end]] = end
            if len(d) > 2:
                min_ind = min(d.values())
                start = min_ind + 1
                del d[s[min_ind]]
            max_len = max(max_len, end-start + 1)
            end += 1
        return max_len
            
            
        
        
        
        
# s = ccaabb"

# start, end, dic , max_len
# keep track char
# char end is added and where is it at its at the end
# if our dictionary has more than one of the char, del from d the min values
#  max of from max_len of char
# return the max_len

https://www.youtube.com/watch?v=odSP7QrlJys
