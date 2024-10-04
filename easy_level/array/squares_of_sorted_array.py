class Solution:
    def sortedSquares(self, nums):
        # Initialize the result array
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        pos = len(nums) - 1  # Position for the largest element

        # Two pointer technique
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1  # Fill result array from the end

        return result
