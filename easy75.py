"""
Strings
"""
#1768. Merge strings alternately 

class Solution:
    def mergeAlternately(word1, word2):
      res = []
      i, j = 0,0

      for i < len(word1)) and j < len(word2)):
          res.append(word1[i])
          res.append(word2[i])
          i += 1
          j += 1
      res.append(word1[i:])
      res.append(word2[j:])
      return ''.join(res)


      


        
      
