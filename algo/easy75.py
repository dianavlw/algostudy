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


#1431 Kids with the Greatest Number of Candies

class Solution: 
    def kidsWithCandies(candies, extraCandies):
        maxCandies = max(candies)
        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return True


#605. Can Place Flowers

class Solution:
    def canPlantFlowers(flowerbed, n):
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i + 1 ] == 0):
                flowerbed[i] = 1
                coumt += 1
            if count >= n:
                return True
        return count >= n

#second solution: neetcode

class Solution:
    f = [0] + flowerbed + [0]

    for i in range(1, len(f)-1):
        if f[i-1] == 0 and f[i] ==0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <=0

# 345 Reverse vowels of a string

class Solution:
    def reverseVowels(s):
        vowels = set("aeiouAEIOU")
        s = list(s)

        l, r = 0, len(s)-1
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)











