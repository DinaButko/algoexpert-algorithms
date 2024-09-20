array = [1, 2, 3, 4, 5, 6, 8, 9]

# First solution
def sortedSquaredArray(array):

    # Square each element
    new_array = [num ** 2 for num in array]

    # Sort the squared array
    new_array.sort()  # This sorts the list in place
    return new_array  # Return the sorted list


print(sortedSquaredArray(array=array))

# Second solution
# O(nLogn) time | O(n) space
def sortedSquaredArray(array):
    # Create a new list to hold the squares of the original array's elements.
    # Initialize with zeros, having the same length as the input array.
    sortedSquares = [0 for _ in array] #sortedSquares = [0, 0, 0, 0, 0]

    # Iterate over each element in the input array by index.
    for idx in range(len(array)):
        value = array[idx]  # value = array[0] = -4
        sortedSquares[idx] = value * value # 16 # Square the value and store it in the corresponding position in sortedSquares.

    # Sort the list of squared values in ascending order.
    sortedSquares.sort()

    # Return the sorted list of squared values.
    return sortedSquares


# Third most optimal solution
def sortedSquaredArray(array):
    # Write your code here.

    sortedSquares = [0 for _ in array]

    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:

            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares