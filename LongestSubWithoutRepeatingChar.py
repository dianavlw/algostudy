
  
-------------------------- Longest Substring Without Repeating Characters --------------------------
"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
------ SOLUTION --------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub ={}
        start = cur_length = longest = 0
        
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= start:
                start = sub[letter] + 1
                cur_length = i -sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                cur_length += 1
                if cur_length > longest:
                    longest = cur_length
        return (longest)
        
        
        """The longest substring is a string of letters that go on without repeating

Find the length of the substring
S = “abcabcbb”

Breaking it down = abc abc b b
LongestSub = abc 

Output: 3

ABC length is 3 

Iterate through the string
Set? Count each char that I find
Return the count and char 
Return a new string with new characters 
If nothing return 0

question: are there any space or special characters?
Should I add them to my solution?"""
