class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base case: if n is less than or equal to 0
        if n <= 0:
            return False
        # Base case: if n equals 1
        if n == 1:
            return True
        # If n is even, divide it by 2 and make a recursive call
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        # If n is odd and greater than 1, return False
        return False
