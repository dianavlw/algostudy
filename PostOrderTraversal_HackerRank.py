"""
HackerRank
Tree: POSTORDER Traversal:
    
Complete the POSTORDER function in the editor below. It received 1 parameter: a pointer to the root of a binary tree.
It must print the values in the tree's postorder traversal as a single line of space-separated values.
  
  Print the tree's POSTORDER traversal as a single line of space-separated values.
      
        1
         \
          2
            \
              5
            /   \
           3      6
            \
              4
  Sample Output:
    4 3 6 5 2 1
    
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

----------- SOLUTION ------------

def postOrder(root):
    #Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root, end=" ")

      
        
