"""
1119. Remove Vowels from a String: https://leetcode.com/problems/remove-vowels-from-a-string/

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.


Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
"""
class Solution:
    def removeVowels(self, s: str) -> str:
        retval = ''
        for letter in s:
            if letter not in 'aeiou':
                retval += letter 
        return retval 
    
#  vowels:aeiou
# for letter in s check to see the letter is not in aeiou
# if its not in the s then continue to traverse and retrun the char not in s


