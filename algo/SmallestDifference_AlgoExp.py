"""Source: https://www.algoexpert.io/questions/Smallest%20Difference
Smallest Difference:

arrayOne=[-1,5,10,20,28,3]
arrayTwo=[26,134,135,15,17]
Sample Output = [28, 26]

# soft both arrays
arrayOne=[-1,3,5,10,20,28]
arrayTwo=[26,134,135,15,17]

have two pointers get the difference 
move pointer ex -1 < 15 
move arrayOne Pointer to -> and update the difference 
"""

def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float('inf')
	current = float('inf')
	
	smallestPait = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair







