

-------------------------------- Number of ways to Traversee Graph --------------------------------
"""
#RECURSIVE:
Time: O(2^(n+m))
Space: O(n+m)
	n = width
	m = height
"""
# SOLUTION 1

def numberOfWaysToTraverseGraph(width, height):
	if width == 1 or height == 1:
		return 1
	return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height -1)
--------------------------------
"""
#DYNAMIC PROGRAMMING
Time: O(n*m) loop through all rows and col
Space: O(n*m) data is being stored
"""	
# SOLUTION 2

#DYNAMIC PROGRAMMING
Time: O(n*m) loop through all rows and col
Space: O(n*m) data is being stored
	
def numberOfWaysToTraverseGraph(width, height):
	numberOfWays = [[0 for _ in range(width +1] for _ in range(height + 1)]
	
	for w in range(1, width + 1):
 	    for h in range(1, height + 1):				  
		if w ==1 or h == 1:
		  numberOfWays[h][w] =1
		else:
		  waysLeft = numberOfWays[h][w-1]
		  waysUp = numberOfWays[h-1][w]
		  numberOfWays[h][w] = waysLeft + waysUp
	return numberOfWays[h][w]
					  
 --------------------------------------- ALGORITHMS ---------------------------------------



"""
MIT OpenCourseWare: https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-notes/
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02_orig.pdf
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf
  

What is an Algorithm?

Copmputational procedure for solving a problem
input -> alg -> output

Computer Program -> algorithm
build out of programming language: -> write them in pseudocode/structure english
Computer -> model of computation

Model of Computation
- Specifies what operations on algorithm is allowed
- cost(time...) of each app.

1. Random Access Machine (RAM)
  - arrays
  -Random Access Memory memory by big array
  -in O(i) an algorithm can read in constant number of words do constant computations
  and store in constant words and constant registers
  -O(i) = constant time
  - word is w bits

2. Pointer Machine aka references
- dynamically allocated objects
-objects has O(1) fields
-fields = word(eg. int)
- pointer points to another objects or null or none
- example linked list, no matter how long your linked list is its constant time

Python Model:
  1. "List" = array
  2. Object with O(1) attributes 
  - x = x.next this takes constant time no matter how many object is
  L.append(x) copy and past will take linear time
  table doubling will be done in constant time operation 
  c = l1 + l2  known as:
    L = []
    for v in L1:
      L.append(x)
    for x in L2:
      L.append(x)
      
this takes constant time
to build an initial list

QUESTIONS:
x in L = linear time
scan through finding the item 
how long to compute the lenght of the list = Constant time, in python have a counter build in
how long to store a list? = n(logN) N is the lenght of the list, time to compare the items

Dictionaries (DICT)
D[key] = val -> O(1)

Long = 
x + y  how long does it take to add them if |x| |y| long?
O(|x| + |y|)

x * y
O(|x| + |y|)log3)
lg = log2


Source: https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb 
    
Sorting:
  https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf
Why sorting?
Recurence solving, Organize mp3, maintain a telephone directory

Problems that become easy once items are in sorted order:
  -find median, or find closest pairs
  -binary search, identify statictical outliers
Non Obvious applications:
  -data compression, sorting find duplicates
  -computer graphic, rendering front to back 
 

INSERTION SORT: https://www.geeksforgeeks.org/insertion-sort/
    Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
    The array is virtually split into a sorted and an unsorted part. 
    Values from the unsorted part are picked and placed at the correct position in the sorted part.

Constant time if you have a sorted list    
Run Time?: O(N^2) because of the swaps    
Space: O(1)
  
Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
  
    
 def insertionSort(array):
	index_length = range(1, len(array))
	for i in index_length:
		values_to_sort = array[i]
		
		while array[i-1] > array[i] and i > 0:
			array[i], array[i-1] = array[i-1], array[i]
			i= i-1
	return array
		
 BINARY INSERTION SORT: https://www.geeksforgeeks.org/binary-insertion-sort/
We can use binary search to reduce the number of comparisons in normal insertion sort. 
Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration. 
In normal insertion sort, it takes O(n) comparisons (at nth iteration) in the worst case. 
We can reduce it to O(log n) by using binary search. Finding a specific item in an array
  
  
  Algorithm:
    # Time: O(long(n)) 
    # Space: O(1)
    def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)
"""
def binarySearchHelper(array, target, left, right):
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]
		if target == potentialMatch:
			return middle
		elif target < potentialMatch:
			right = middle - 1
		else:
			left = middle + 1
	return -1
		
  # Python Program implementation
# of binary insertion sort
 
 
def binary_search(arr, val, start, end):
     Time Complexity: The algorithm as a whole still has a running worst-case running time of O(n2)
     because of the series of swaps required for each insertion. 
    # we need to distinugish whether we
    # should insert before or after the
    # left boundary. imagine [0] is the last
    # step of the binary search and we need
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    # this occurs if we are moving
    # beyond left's boundary meaning
    # the left boundary is the least
    # position to find a number greater than val
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
 
 
print("Sorted array:")
print(insertion_sort([37, 23, 0, 31, 22, 17, 12, 72, 31, 46, 100, 88, 54]))
 
"""	
# Code contributed by Mohit Gupta_OMG
		
  data n^2 for both
 
  compare vs swaps, equal in cost, in num are same in cost
  
  ex. compares >> swaps O(n^2) comparission cost
  simple fix for this algo gives a simple complexity, data of compares? BINARY SEARCH
  number of compares, replace it with binary search 
  Do binary search A[0: l-1] already sorted in O(logi) Time
  
Merge Sort:
  Divide and Conquer
  Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
  It assumes two sorted arrays as input.
  l1    r1
  20    12
  13    11
  7     9 -- 2 --9 --> 2
  2     1 --> 1
 compare 2 and 1, then 2 and 9, then 7 and 9, 9 and 11, ect. 
  which is smaller?
  1 2 7 9 11 12 13 20  
  It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
  The merge() function is used for merging two halves. 
  The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
  See the following C implementation for details.
  
  
  MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
The following diagram from wikipedia shows the complete merge sort process for an example array {38, 27, 43, 3, 9, 82, 10}. 
If we take a closer look at the diagram, we can see that the array is recursively divided into two halves till the size becomes 
1. Once the size becomes 1, the merge processes come into action and start merging arrays back till the complete array is merged.
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
T(n) = 2T(n/2) + θ(n)

What is one advantage of insertion sort over merge sort?
-auxilirary space: 
merge sort O(n) auxiliary space
in space sort => O(1) auxiliary space

insertion has the advantage


4. Heaps and Heap Sort: https://www.youtube.com/watch?v=B7hVxCmfPtM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=4
notes: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf
    
    PRIORITY QUEUE:
Implements a set S of elements, each of elements. A data structure implementing a set S of element, 
each associated with a key, supporting the following operations.

insert(S,x): insert element x into set S
max(S): return element of S with largest key
extract_max(S): return element of S with largest key and remove from S
increase_key(S,x,k): increase the value of element x's key to new value k
  
  HEAP:
  Implementation of a priority queue
  an array, visualize as a nearly completed binary tree
  Max Heap Property: The key of a node is >= than the kesy of its children
  Min Heap defined analogously 
  
  HEAP as a TREE:
    root of tree: first element in the array, corresponding to i = 1
    parent(i) =i /2 : return index of node's parent
    left(i) = 2i: return index of node's left child
    right(i) = 2i + 1: return index of node's right child
  
    
 """ 
  
  
  
  
  
  -------------------- A love Letter ----------------------
""""
This is from Pramp: I thought it was going to be a much simpler algorithm but no once I took a look
at the actual result I realized I knew so little on ascii so once again this is from PRAMP.COM

Anonymous Love Letter
You have written an anonymous love letter and you don’t want your handwriting to be recognized. 
Since you don’t have a printer within reach, you are trying to write this letter by copying and pasting characters from a newspaper.

Hints:
This demo question if fairly simple. Ready for our real interview problems? Get Started.
If your peer is stuck, ask how would you know if you can write L by using the letters in N only. Try to get them to emulate the naive algorithm to this supply & demand problem and then to formalize it.
If you peer uses a hash table, make sure they understand what hashing means and what it involves. Then ask what can be a little more efficient. If it doesn’t ring a bell, ask what else do we know about these characters that would help us to use something similar to hashing, only more basic and efficient.
Checking if 256 character counts are 0 after each and every character scanned in N is not a good practice, if your peer does that try to give hints towards a simpler approach instead, like the one showed with charCount.
Sorting and searching are an overkill and should be avoided when the linear solution is that simple.
Any solution that takes more than linear O(n+m) runtime is not acceptable as complete.

SOLUTION::
Given a string L representing the letter and a string N representing the newspaper, return true if the L can be written entirely from N and false otherwise. The letter includes only ascii characters.
Anonymous Love Letter
L can be written by characters from N, if and only if every character in L is included in N at least by the same number of occurrences. 
To determine that, we should count the number of occurrences for each character in L and determine if we have all of them, at least at the same quantity in N. 
A good approach to do this is using a hash table. The hash key would be the character, and the hash value would be the number of occurrences counted so far.

Since all characters are ascii we can avoid the hash table and use a simple array of 256 integers, that we’ll name charMap. 
Every index in charMap will hold the number of occurrences of the character represented by its ascii code.
Since N is most likely much longer than L, we start with counting the number of character occurrences in it first. 
That way, we’ll be able to stop processing N once we find all of L's characters in it, and reduce computational costs.

After counting all character occurrences in L, we scan N and for each character, reduce its count on charMap if it is larger than 0. 
If all counts in charMap are zero at some point, we return true. Otherwise, if we are done scanning N and at least one count is not 0, we return false.

Pseudocode:

function isLoveLetterReproducible(L, M):
   charMap = []
   charCount = 0

   for i from 0 to L.length:
      charCode = int(L.charAt(i)) 
      if (charMap[charCode] == 0):
         charCount++
      charMap[charCode]++

   for i from 0 to N.length:
      charCode = int(N.charAt(i))
      if (charMap[charCode] > 0):
         charMap[charCode]--
         if (charMap[charCode] == 0):
            charCount--
      if (charCount == 0):
         return true

   return false
Time Complexity: In the worst case we scan all of L and N linearly. For each character we execute a constant number of operations. 
Therefore, if m and n are the lengths of L and N, the runtime complexity is linear O(n+m).

Space Complexity: Using the variable charCode is only to make the pseudocode above clearer and can be avoided (by using the value directly). 
Other than that, since we use an array of constant size (256) and a constant number of variable, the space complexity is O(1).
""""
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
