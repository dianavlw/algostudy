Prompt:
""" 1. SUBSET / KNAPSACK (like maximizeCPU)
Given an array of integers and a target, return the largest sum you can make that is <= target. 
Each number can be used once."""

""" Example:
nums = [3, 5, 8]
target = 10
-> output : 8
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
    possible_sums{0}

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
  """
  4. Count Factors
  """
  """
  5. Largest Factor Less than n
  """
  """
  6. Sum of Factors
  """
