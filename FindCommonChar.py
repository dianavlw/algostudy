"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

# Solutions are references from leetcode, this is how i like to review by viewing others work and applying to my owncode.
# Solution 1.
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
            for c in set(A[0]):
                count = A[0].count(c)
                occurences = 1
                for i in range(1,len(A)):
                    if c in A[i]:
                        count = min(count,A[i].count(c))
                        occurences += 1
                    else:
                        break
                if occurences == len(A):
                    for i in range(count):
                        result.append(c)

            return result
# Solution 2.
def commonChars(self,A):
        check = list(A[0])
        for word in [A:]:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check
