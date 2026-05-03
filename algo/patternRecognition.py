
""" 1. SUBSET / KNAPSACK (like maximizeCPU)
Given an array of integers and a target, return the largest sum you can make that is <= target. 
Each number can be used once."""

""" Example:
nums = [3, 5, 8]
target = 10
-> output : 8
"""

"""
1. Closest Sum <= Target
"""
def closest_sum(nums, target):
    possible_sums = {0}  # start with sum = 0

    for num in nums:
        new_sums = set()  # sums formed using current num
        for curr in possible_sums:
            if curr + num <= target:
                new_sums.add(curr + num)

        possible_sums.update(new_sums)

    return max(possible_sums)

  
"""
  2. Can you reach the Target?
"""
def can_reach_target(nums, target):
    possible_sums={0}

    for num in nums:
      new_sums = set()
      for curr in possible_sums:
        if curr + num <= target:
          new_sums.add(curr + num)
      possible_sums.update(new_sums)
      
    return target in possible_sums
"""
  3. Count Possible Sums <= Target
"""

def count_possible_sum(nums, target):
    possible_sums={0}

    for num in nums:
        new_sum = set()
        for curr in possible_sums:
            if curr + num <= target:
                new_sums.add(curr + num)
        possible_sums.update(new_sums)
    return len(possible_sums)
    
    
"""

  4. Count Factors

"""

def count_factors(n):
    count = 0
    i = 1

    while i *i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count 


"""
  5. Largest Factor Less than n
"""
def largest_factor_less_than_n(n):
    if n<=1:
        return 0
    i = 2
    while i * i <=n:
        if n % i == 0:
            return n//i
        i += 1
    return 1

"""
  6. Sum of Factors
"""
def sun_of_factors(n):
    total = 0
    i= 1

    while i * i <=n:
        if n % i == 0:
            total += i
            if i != n// i:
                total += n // i
        i += 1
    return total 


"""
Frequency map template
"""
def count_freq(nuns):
    freq = {}

    for num in nuns:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


"""
two sum template
nums = [1, 2, 3]
target = 4
"""

def two_sum(nums, target):
    seen = {} # keep track of nums we looped

    for i, n in enumerate(nums):
        possible_num = target - num
        if possible_num in seen:
            return [seen[possible_num], i]
            seen[n] =i
        return []


# first occurence
def first_occurence(nums, target):
    dict = {}
    for i, n in enumerate(nums):
        if n == target:
            return i
        dict[n] == i
    return -1

#last occurence 
def last_occurence(nums, target):
    last = -1
    for i, n in enumerate: 
        if n == target:
            last = i
    return last

#count_occurence
def count_occ(nums, target):
    count = 0
    for n in nums:
        if n == target:
            count += 1
    return count 

#fid all indicies of target
def findAllIndicies(nuns, target):
    result = []
    for i, n in enumerate(nums):
        if n == target:
            result.append(i)
    return result 

# Subarray sum equals k 
#problem : given an array nums and an integer k, return how many continuos subarrays sum to k. 
# nums = [1, 2, 3]
# target = 3
# [1, 2] = 3
#[3] = 3
# output = 2

def subarraySum(nums, k):
    prefix_count = {0: 1}
    curr_sum = 0
    count = 0

    for n in nums:
        curr_sum += n

        need = curr_sum - k

        if need in prefix_count:
            count += prefix_count[need]

        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

    return count
        
        
        
#maxSubArray    
def maxSubArray(nums):
    cur_sum = 0
    max_sum = float('-inf')
    n = len(nums)

    for i in range(len(n)):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum 
#OR
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0 
        max_sub = nums[0]

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum+= n
            max_sub = max(max_sub, curr_sum)
        return max_sub
    
#643. Maximum Average Subarray I

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for i in range(len(nums)-k):
            curr_sum += nums[i+k] - nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum /k



#https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/maximum-non-overlapping-intervals/problem?isFullScreen=true
# Maximum number of non-overlapping intervals

def maxNonOver(meetings):
    meetings.sort(key=get_num)
    count = 0
    last_num = float("-inf")

    for start, end in meetings:
        if start >= last_num:
            count += 1
            last_num = end
    return count

def get_num(meeting):
    return meeting[1]

    
#435. merge Intervals

def merge(intervals):
    intervals.sort()
    if intervals == []:
        return []
    result =[]
    
# [[1, 3], [2,6],[8,10],[15,18]]
    #result = [[1,3]]

    for interval in intervals:
        if result == [] or result[1][-1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result
    
        
#435 Non-overlapping intervals
#https://leetcode.com/problems/non-overlapping-intervals/

def eraseOverlapIntervals(intervals):
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]

    for start, end in intervals:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res 

    
"""
3 affirm qs
We need return the p-th smallest factor of n.

Example:
n = 10, factors are:

1, 2, 5, 10

If p = 3, answer is 5.

Because n can be huge, up to 10^15, we should not loop from 1 to n.
"""

def pthFactor(n, p):
    small = []
    large = []

    i = 1
    #we start at 1 b/c 0 is not a valid divisor
    while i * i <= n: #“What numbers should I test as possible factors?” not “How many elements are there?” (while i < len(n))
        # 1 * 1 <=n
        if n % i == 0:
            #10 % 1 == 0
            small.append(i)
            if i != n // i:
                #1 != 10 //1
                #small[1]
                large.append(n // i)
                #10//1
                #large,[10]
        i += 1

    factors = small + large[::-1]

    if p > len(factors):
        return 0

    return factors[p - 1]



"""
this problem is asking:

Given task sizes, pick some tasks so their total is as large as possible without going over processingCapacity.

Each task can be used once.

Example:

requirements = [2, 9, 7]
processingCapacity = 15

Possible sums:

2
9
7
2 + 9 = 11
2 + 7 = 9
9 + 7 = 16 too big
2 + 9 + 7 = 18 too big

Best valid answer is:

11
"""


def maximizeCPU(requirements, processingCapacity):
    possible = {0}

    for task in requirements:
        new_sums = set()

        for total in possible:
            new_total = total + task

            if new_total <= processingCapacity:
                new_sums.add(new_total)

        possible.update(new_sums)

    return max(possible)


"""
This is asking for a length 3 subsequence like this:

chosen[0] < chosen[1] > chosen[2]

So the middle number must be bigger than the left and right numbers.

We want the smallest possible sum.

Example:

arr = [3, 4, 2, 6, 1, 1, 1]

One valid subsequence is:

[3, 4, 1]

Because:

3 < 4 > 1

Sum:

3 + 4 + 1 = 8

Answer is 8.

"""

def getMinimumSum(arr):
    n = len(arr)

    left_min = [float('inf')] * n
    right_min = [float('inf')] * n

    # smallest number before each index
    smallest = float('inf')
    for i in range(n):
        left_min[i] = smallest
        smallest = min(smallest, arr[i])

    # smallest number after each index
    smallest = float('inf')
    for i in range(n - 1, -1, -1):
        right_min[i] = smallest
        smallest = min(smallest, arr[i])

    answer = float('inf')

    for i in range(n):
        middle = arr[i]

        if left_min[i] < middle and right_min[i] < middle:
            total = left_min[i] + middle + right_min[i]
            answer = min(answer, total)

    if answer == float('inf'):
        return -1

    return answer


    






