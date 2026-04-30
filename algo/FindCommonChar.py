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

# Solutions are references from leetcode
# Solution 1.
class Solution:
    def commonChars(self, n: List[str]) -> List[str]:
        l =len(n)
        d = {}

        for x in n:
            for y in set(x):
                if y not in d:
                    d[y] = [x.count(y)]
                else:
                    d[y].append(x.count(y))
        res = []
        for x, y in d.items():
            if len(y) >= l:
                z = min(y)
                if z > 1:
                    for _ in range(z):
                        res.append(x)
                else:
                    res.append(x)
        return(res)
