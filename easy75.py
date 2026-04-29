"""
Strings
"""
#1768. Merge strings alternately 

class Solution:
    def mergeAlternately(self, word1, word2):
        res = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])

        return ''.join(res)



data = Solution()
print(data.mergeAlternately("ABCDEF", "GHIJK"))  # Expected: "AGBHCIDJEKF"


      
#1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1
            return ""
        a, b = len(str1), len(str2)

        while b > 0:
            a, b = b , a % b
            
        return str1[:a]

        
sol = Solution()

print(sol.gcdOfStrings("ABCABC", "ABC"))   # Expected: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Expected: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Expected: ""      
