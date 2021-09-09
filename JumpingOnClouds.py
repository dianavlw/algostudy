
"""
HackerRank Interview Preparation Kit > Warm-up Challenges
: JUMPING ON THE CLOUDS
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.
For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
Example: 
c = [0,1,0,0,0,1,0]
Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: 0 -> 2 -> 4 -> 6  or 0 -> 2 -> 3 -> 4 -> 6 . The first path takes 3 jumps while the second takes 4. Return 3.
Sample Input: 
7
0 0 1 0 0 1 0
Sample Output:
4
"""

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    c. append(1)
    if len(c) < 3:
        return 0
    i = 0
    while i < len(c) -2:
        if c[i +2] == 0:
            i += 2
        else:
            i += 1
        jump += 1
    return jump    
    
"""
    jumps = 0
    current = 0
    while current < len(c):
        if current + 2 > len(c) and c [current + 2] == 0:
            jumps += 2
            current += 2
        elif current +1 < len(c) and c[current + 1] == 0:
            jumps += 1
            current += 1
        else:
            current += 1
"""



