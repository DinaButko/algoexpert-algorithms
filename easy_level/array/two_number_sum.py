# First solution two for loops
# O(n^2) time | O(1) space
from typing import List


def twoNumberSum(array, targetSum):
    # Write your code here.

    for i in range(len(array) - 1):  # 4 ,means from 0 to 4
        firstNum = array[i]

        for j in range(i + 1, len(array)):  # 5 from 0 to 4
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


twoNumberSum(array=[3, 5, -4, 8, 11], targetSum=8)


# Leetcode task where we want return indexes of values

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Hash table solution
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# With index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}

        for index, number in enumerate(nums):
            potentialValue = target - number

            if potentialValue in numbers:
                return [numbers[potentialValue], index]  # Return the indices
            else:
                numbers[number] = index  # Store the index of the number

        return []  # Return an empty list if no solution is found