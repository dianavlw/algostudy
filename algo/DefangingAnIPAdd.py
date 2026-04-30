"""
1108. Defanging an IP Address: https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        answerString = ""
        for c in address:
            if c == ".":
                answerString += "[.]"
            else:
                answerString += c
        
        return answerString
        
        
