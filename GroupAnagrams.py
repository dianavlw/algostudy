"""
GROUP ANAGRAMS: https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
https://www.youtube.com/watch?v=n3V-wvCXDCs
1. empty dic
2. loop through array
3. sort every word, check if the sorted word is in the dict.
4. if not add it to the dict taking the sorted word as key and word as value, if yes append it 
5. loop through the dict and print all the values of dict. 
O(m* nlogn) =(to sort the strings)

M= length of each string

"""
# empty dict and the key is the sorted letters of each str 
#ex. {aet:[eat,tea,  } we will append the values and return them in the result.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))

            if sortedword not in dict:
                dict[sortedword] = [word]

            else:
                dict[sortedword].append(word)
            
        
        result = []
        for item in dict.values():
            result.append(item)
        return result
