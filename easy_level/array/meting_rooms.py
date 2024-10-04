from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                next_value = nums2[j]
                nums1.append(next_value)
        print(nums1)
        return nums1


test = Solution()
test.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
