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
