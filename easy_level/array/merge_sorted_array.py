def merge(nums1, m, nums2, n):
    # Set up three pointers, starting from the end
    p1 = m - 1  # Pointer for nums1 (elements to be merged)
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the final position in nums1

    # Iterate until all elements from nums2 are merged
    while p2 >= 0:
        # If nums1 still has elements left and nums1[p1] is greater, place it in nums1[p]
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            # Otherwise, place nums2[p2] in nums1[p]
            nums1[p] = nums2[p2]
            p2 -= 1
        # Move the pointer for the final position backward
        p -= 1
