def bubbleSort(array):
    # Flag to keep track if the array is sorted
    isSorted = False
    # Continue the loop until no more swaps are needed
    while not isSorted:
        # Assume the array is sorted; if we find a pair that needs swapping, we'll set this to False
        isSorted = True

        # Loop through the array up to the second-to-last element
        for i in range(len(array) - 1):
            # If the current element is greater than the next, swap them
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)  # Call swap function
                # After a swap, we know the array was not sorted, so set this to False
                isSorted = False
    return array


def swap(i,j, array):
    array[i], array[j] = array[j], array[i]



# leetcode task

from collections import Counter
from typing import List


class Solution:

    def swap(self, i, j, array):
        # Correcting the swap logic
        array[i], array[j] = array[j], array[i]

    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each number
        frequency = Counter(nums)  # This gives us a frequency dictionary

        isSorted = False
        counter = 0  # Tracks how much of the array is already sorted

        # Step 2: Implement Bubble Sort with frequency-based logic
        while not isSorted:
            isSorted = True

            # Bubble sort logic: compare based on frequency, then by value
            for i in range(len(nums) - 1 - counter):
                # Compare frequencies first
                if frequency[nums[i]] > frequency[nums[i + 1]]:
                    # If frequency is higher, swap
                    self.swap(i, i + 1, nums)
                    isSorted = False
                # If frequencies are the same, sort by value in decreasing order
                elif frequency[nums[i]] == frequency[nums[i + 1]] and nums[i] < nums[i + 1]:
                    # If the value is lower but frequencies are the same, swap
                    self.swap(i, i + 1, nums)
                    isSorted = False

            # Increment counter to reduce the number of comparisons in the next pass
            counter += 1

        return nums  # Return the sorted array (not [nums])

