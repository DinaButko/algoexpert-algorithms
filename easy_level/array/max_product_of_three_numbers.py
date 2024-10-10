from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # O(nlogn)
        # O(1 or O(n)
        # Sort the array
        nums.sort()

        first = nums[-3] * nums[-2] * nums[-1]  # Product of the three largest numbers
        second = nums[0] * nums[1] * nums[-1]  # Product of the two smallest and the largest number

        return max(first, second)
