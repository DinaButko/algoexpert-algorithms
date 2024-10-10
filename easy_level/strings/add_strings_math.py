class Solution:
    #Time Complexity: O(max(m, n))
    #Space Complexity: O(max(m, n))
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        # Loop until both strings are processed
        while i >= 0 or j >= 0 or carry:
            # Get current digits
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            # Calculate sum of the digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10  # Update carry for the next position
            result.append(str(total % 10))  # Append the last digit of total to result

            # Move to the next digits
            i -= 1
            j -= 1

        # The result is built in reverse order, reverse it before returning
        return ''.join(result[::-1])