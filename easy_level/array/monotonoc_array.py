from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        # Initialize two flags to check both increasing and decreasing order
        increasing = decreasing = True

        # Iterate through the list
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False  # If an element is greater than the previous, it's not decreasing
            if nums[i] < nums[i - 1]:
                increasing = False  # If an element is less than the previous, it's not increasing

        # If either increasing or decreasing remains True, then the list is monotonic
        return increasing or decreasing