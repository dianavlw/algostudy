Source: https://www.algoexpert.io/questions/Monotonic%20Array
    
"""
Definition: mon·o·ton·ic
/ˌmänəˈtänik/
Learn to pronounce
adjective
1. MATHEMATICS: (of a function or quantity) varying in such a way that it either never decreases or never increases.

Monotonic Array:
array: [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
Output: True

Write a function that takes in an array of integers returns a boolean.
Non-increasing elements arent necessarily exclusively decreasin they simply dont increase. non decreasing elements are
necessarily exclusively increasing, they simply dont decrease.
"""

# SOLUTION 1:
	
def isMonotonic(array):
	if len(array) <= 2:
		return True
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i-1]
			continue
		if breaksDirection(direction, array[i-1], array[i]):
			return False
	return True

def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0

# SOLUTION 2:
def isMonotonic(array):
    isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False
	return isNonDecreasing or isNonIncreasing 



