"""
170. Two Sum III - Data structure design
Design a data structure that accepts a stream of integers 
and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists 
any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]
"""


class TwoSum(object):

    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.num_counts = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums_count:
            need = value - num

            if num != need:
                if need in self.nums_count:
                    return True
            elif self.nums_count[num] > 1:
                return True

        return False
    
    #OR with .keys()
"""     for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True

        return False"""

"""
        for i in self.nums:
            if value-i in self.nums:
                if i==value-i and self.nums[i]==1:
                    continue
                return True
        return False
"""