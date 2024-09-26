def binarySearch(array, target):
    # This function initiates the binary search process.
    # It calls the binarySearchHelper function, passing the array, target,
    # and the initial indices (0 for left and len(array)-1 for right).

    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    # This function performs the actual binary search using iteration.
    # It takes the array, the target value to find, and the left/right bounds as input.

    while left <= right:
        # The loop continues as long as the left pointer is less than or equal to the right pointer,
        # meaning there are still elements to search within the bounds.

        # Calculate the middle index of the current search range.
        middle = (left + right) // 2

        # Get the element at the middle index.
        potentialMatch = array[middle]

        # Check if the target matches the middle element.
        if target == potentialMatch:
            # If a match is found, return the index of the target.
            return middle

        # If the target is smaller than the middle element,
        # search the left half of the current array by updating the right pointer.
        elif target < potentialMatch:
            right = middle - 1

        # If the target is greater than the middle element,
        # search the right half by updating the left pointer.
        else:
            left = middle + 1

    # If the loop completes and no match is found, return -1 to indicate the target is not in the array.
    return -1
