"""
Sorted Square Array:
array = [1,2,3,5,6,8,9]
sample output = [1,4,9,25,36,64,81]

"""

# Solution: 
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
	
	for idx in range(len(array)):
		value = array[idx]
		sortedSquares[idx] = value * value
		
	sortedSquares.sort()
    return sortedSquares
