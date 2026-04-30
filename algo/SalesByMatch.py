"""
HackerRank Interview Preparation Kit > Warm-up Challenges
SALES BY MATCH
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
Example
n = 7
ar = [1,2,1,2,1,3,2]
There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
"""


def sockMerchant(n, ar):
    # Write your code here
    count = 0
    d ={}
    
    for i in ar:
        d[i] = d.get(i, 0) + 1
    
    for i in d.keys():
        count += d[i]//2
    return count        
