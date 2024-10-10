class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        leftIndex, rightIndex = 0, len(s) - 1

        while leftIndex < rightIndex:
            if s[leftIndex] != s[rightIndex]:
                # Check both possibilities: skipping left or skipping right
                return is_palindrome_range(leftIndex + 1, rightIndex) or is_palindrome_range(leftIndex, rightIndex - 1)
            leftIndex += 1
            rightIndex -= 1

        return True  # It's a palindrome already
