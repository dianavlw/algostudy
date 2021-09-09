# Note: put this in https://pythontutor.com
#     it will help you understand and test your code

----------------------------------------- Fill the Hard Disk Drive ----------------------------------------- 

 """
 Description:
Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.

Input:
Array of file sizes (0 <= s <= 100)
Capacity of the HD (0 <= c <= 500)
Output:
Number of files that can be fully saved in the HD.

Examples:
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12
save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, but 4+4+4 > 11

Enumerate: https://realpython.com/python-enumerate/#using-pythons-enumerate
(count, value)

Accumelator Pattern:
https://runestone.academy/runestone/books/published/thinkcspy/Strings/TheAccumulatorPatternwithStrings.html

Acuumelator Pattern in string: https://runestone.academy/runestone/books/published/thinkcspy/Strings/TheAccumulatorPatternwithStrings.html
 """
-------- SOLUTION --------
def save(sizes, hd): 
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)
  
-------- SOLUTION --------
# Note: put this in https://pythontutor.com/visualize.html#mode=display
#     it will help you understand and test your code
    
def save(sizes, hd): 
    acc = 0
    for i, item in enumerate(sizes):
        if acc + item > hd:
            return i
        acc += item
    return len(sizes)
