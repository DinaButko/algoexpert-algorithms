from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # Step 1: Get distinct values by converting the list to a set
        distinct_nums = list(set(nums))

        # Step 2: Sort the distinct values in descending order
        distinct_nums.sort(reverse=True)

        # Step 3: Check if we have at least three distinct values
        if len(distinct_nums) >= 3:
            return distinct_nums[2]  # Third maximum value
        else:
            return distinct_nums[0]  # If there are less than 3 distinct values, return the maximum