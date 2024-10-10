class Solution:
    def climbStairs(self, n: int) -> int:

        """
        Time Complexity: O(n)
         Space Complexity: O(1)
         """
        """
        This function calculates the number of distinct ways to climb a staircase with 'n' steps.
        You can either climb 1 step or 2 steps at a time. The problem is essentially calculating
        the nth number in the Fibonacci sequence.
        """

        # If there is only 1 step, there is only 1 way to climb it.
        if n == 1:
            return 1

        # Initialize the first two values in the sequence:
        # 'first' is the number of ways to climb 1 step (which is 1),
        # 'second' is the number of ways to climb 2 steps (which is 2).
        first = 1
        second = 2

        # For more than 2 steps, we calculate the number of ways dynamically
        # by iterating from the 3rd step up to the nth step.
        for i in range(3, n + 1):
            # The number of ways to reach the current step is the sum of the ways
            # to reach the two previous steps (i.e., Fibonacci relation).
            third = first + second
            # Move the sequence forward by updating 'first' and 'second'.
            first = second
            second = third

        # The final value of 'second' will be the number of ways to climb 'n' steps.
        return second
