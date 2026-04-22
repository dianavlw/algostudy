Prompt:
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
def closets_sum(nums, target):
    possible_sums = {0}
  # keep track of the sums start at 0
    for num in nums:
      new_sums = set() #only use once
      for curr in possible_sums:
        if curr + nums <= target:
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
