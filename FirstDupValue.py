"""
First Duplicate Value
Input array: [2,1,5,2,3,3,4]
Output: 2
""" 
# Solution 1.
def firstDuplicateValue(array):
    # Write your code here.
    seen = set()
	for value in array:
		if value in seen:
			return value
		seen.add(value)
	return -1
	
# Solution 2. 
minSecIndex = len(array)
for i in range(len(array)):
    value = array[i]
    for j in range(i + 1, len(array)):
      valueToCompare = array[i]
      if value == valueToCompare:
        minSecIndex = min(minSecIndex, j)
        
if minSecIndex == len(array):
  return -1

return array[minSecIndex]
           
