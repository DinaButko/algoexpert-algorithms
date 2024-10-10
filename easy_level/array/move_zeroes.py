from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeros in the list to the end while maintaining the order of non-zero elements.
        The modification is done in-place.
        """

        # Initialize a pointer to track the position of the last non-zero element.
        last_non_zero = 0

        # First pass: Move non-zero elements to the front.
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]  # Move the non-zero element to the current last_non_zero position.
                last_non_zero += 1  # Update the last_non_zero index.

        # Second pass: Fill the remaining positions in the list with zeroes.
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0  # Set the remaining elements after the last non-zero element to 0.
