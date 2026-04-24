"""
HackkerRank
https://www.hackerrank.com/prep-kit/software-engineer
"""

"""
Arrays and Basic Problem Solving

1. Count Elements Greater than Previous Average
2. Find the Smallest Missing Positive
3. Check Palindrome by Filtering Non-letters
4. Check for non-identical string Rotation
5. Target Index Search
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#
"""
if len(responseTimes) <= 1:
    return 0
    
count = 0
running_sum = responseTimes[0]
       
for n in range(1, len(responseTimes)): 
        avg_sum = running_sum / n
        if responseTimes[n] < avg_sum:
            count += 1
        running_sum += responseTimes[n]
return count 


"""

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    
    count = 0
    running_sum = responseTimes[0]
        
    for n in range(1, len(responseTimes)): 
        avg_sum = running_sum / n
        if responseTimes[n] < avg_sum:
            count += 1
        running_sum += responseTimes[n]
    return count 
    
     
    # if len(responseTimes) <= 1:
    #     return 0
        
    # running_sum = responseTimes[0]
    # count = 0
    
    # for i in range(1, len(responseTimes)):
    #     prev_count = 1
    #     prev_avg = running_sum / prev_count
        
    #     if responseTimes[i] > prev_avg:
    #         count += 1
    #     running_sum += responseTimes[i]
    # return count 


if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
