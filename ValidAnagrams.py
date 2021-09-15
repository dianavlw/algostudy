"""
Valid Anagram: https://leetcode.com/problems/valid-anagram/solution/

Solution
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
        
        for val in counter.values():
            if val!= 0:
                return False
        return True

    """
    return sorter(s) == sorted(t)
    # O(logN)
    
    or
    
    # O(N)
    return Counter(s) == Counter(t)
    
    or
    if len(s) != len(t):
        return False
        
    return sorter(s) == sorte(t)
    
    O(nlog(n)
    O(1)
    
    """
                    
