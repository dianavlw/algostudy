"""
#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

video explanation: https://www.youtube.com/watch?v=iSFZVetUKns
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for char in magazine:
            if char not in chars: 
                chars[char] = 1
            else: 
                chars[char] += 1

        for char in ransomNote:
            if char in chars and chars[char] > 0:
                chars[char] -= 1
            else: 
                return False
        
        return True
      
  #credit : Danish Valmani Leetcode
