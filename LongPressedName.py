"""
925. Long Pressed Name: https://leetcode.com/problems/long-pressed-name/

Your friend is typing his name into a keyboard. 
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
#         Two pointers startig at the beginning of name and typed
#  take the len of both so we can traverse through them
# we increment our pointers when they are less than the array and is both char are the same in order
# else if theyre not the same and theres not chars to traverse, if the char and the previous char are not repeating then return false its not a long pressed name. 
#  increment the second pointer in typed str to continue the loop and return if i is equal to the len(name)
        j = 0
        i = 0
        n = len(name)
        t = len(typed)
        
        while j < t:
            if i < n and name[i] == typed[j]:
                i +=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j +=1
        return i == n
