from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        This function returns the greatest common divisor (GCD) of two strings.
        The GCD of two strings is the largest string that can be repeated to
        construct both str1 and str2.
        """

        # Check if concatenating str1+str2 gives the same result as str2+str1.
        # If not, return an empty string because they don't share a common pattern.
        # Example: "ABC" + "AB" != "AB" + "ABC" -> return ""
        # Time complexity: O(m + n), where m and n are the lengths of str1 and str2.
        # Space complexity: O(m + n) because of the concatenated strings.
        if (str1 + str2) != (str2 + str1):
            return ""  # No common divisor string exists

        # Calculate the greatest common divisor (GCD) of the lengths of str1 and str2.
        # This will give the length of the largest string that divides both str1 and str2.
        maxValue = gcd(len(str1), len(str2))

        # Return the substring from the start of str1 with the length of the GCD.
        # This substring is the largest common divisor string of str1 and str2.
        return str1[:maxValue]


