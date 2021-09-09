"""
Validate Subsequence
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]
output= True
O(n) Time
O(1) Space
"""

def isValidSubsequence(array, sequence):
	arrIdx = 0
	subIdx = 0
	while arrIdx < len(array) and subIdx < len(sequence):
		if array[arrIdx] == sequence[subIdx]:
			subIdx += 1
		arrIdx += 1
	return subIdx == len(sequence)





