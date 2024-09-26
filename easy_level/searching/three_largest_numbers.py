
def findThreeLargestNumbers(array):
    # Initialize an array of size 3 to hold the three largest numbers found so far.
    # All positions are set to None initially since we haven't started comparing numbers yet.
    three_largest_array = [None, None, None]

    # Iterate through each number in the input array.
    for num in array:
        # For every number in the array, we update the three_largest_array
        # by passing the current number to the update_largest function.
        update_largest(three_largest_array, num)

    # Return the array containing the three largest numbers, sorted in ascending order.
    return three_largest_array

def update_largest(three_largest_array, num):
    # Check if the current number is greater than the largest number (stored at index 2).
    if three_largest_array[2] is None or num > three_largest_array[2]:
        # If the current number is greater than the largest, update the largest value (index 2).
        shift_and_update(three_largest_array, num, 2)

    # If the current number is not larger than the largest, check the second largest (index 1).
    elif three_largest_array[1] is None or num > three_largest_array[1]:
        # If the current number is larger than the second largest, update at index 1.
        shift_and_update(three_largest_array, num, 1)

    # Finally, if the number isn't larger than the largest or second largest, check the third (index 0).
    elif three_largest_array[0] is None or num > three_largest_array[0]:
        # If the current number is larger than the third largest, update at index 0.
        shift_and_update(three_largest_array, num, 0)
def shift_and_update(array, num, index):
    # Loop through the array from the first element up to the specified index.
    for i in range(index + 1):#  # range(3) gives: 0, 1, 2
        # When we reach the target index, set the value to the new number (num).
        if i == index:
            array[i] = num
        # Before reaching the target index, shift the previous elements to the left
        # by copying the value from the next index.
        else:
            array[i] = array[i + 1]
