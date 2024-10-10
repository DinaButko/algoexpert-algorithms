class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        # Initialize the result list
        missing_ranges = []

        # Start from the lower boundary
        start = lower

        # Loop through the numbers in nums
        for num in nums:
            if num > start:  # Check if there is a gap
                if num - 1 == start:
                    # If the gap is exactly 1, add only the missing number
                    missing_ranges.append([start, start])
                else:
                    # If there is a range, add the range
                    missing_ranges.append([start, num - 1])

            # Update start to the next number after current
            start = num + 1

        # Check for any missing numbers between start and upper
        if start <= upper:
            if start == upper:
                missing_ranges.append([start, start])
            else:
                missing_ranges.append([start, upper])

        return missing_ranges