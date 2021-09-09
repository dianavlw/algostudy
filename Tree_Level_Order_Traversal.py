
---------- Tree: Level Order Traversal------------
"""
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. 
In level-order traversal, nodes are visited level by level from left to right. 
Complete the function levelOrder and print the values in a single line separated by a space.
https://www.youtube.com/watch?v=568Jr8Fs6jQ

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output

1 2 5 3 6 4
"""
---------SOLUTION------------
def levelOrder(root):
    #Write your code here
    q = []
    q.append(root)
    while len(q)!=0:
        root=q.pop(0)
        print(root.info, end=' ')
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
    
