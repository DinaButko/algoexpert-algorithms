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



from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash table to store the number and its index
        table = {}

        for i, num in enumerate(nums):
            # Calculate the potential match
            potentialMatch = target - num

            # Check if potential match exists in the table
            if potentialMatch in table:
                # Return indices of the two numbers
                return [table[potentialMatch], i]
            else:
                # Store the index of the current number
                table[num] = i

        # If no match found, return an empty list
        return []
