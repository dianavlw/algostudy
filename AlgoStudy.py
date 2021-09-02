
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
  
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
