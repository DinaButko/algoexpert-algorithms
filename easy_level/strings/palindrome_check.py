# First solution
# O(n^2) time | O(n) space
def isPalindrome(string):
    # Initialize an empty string to store the reversed version of the input string
    reversedString = ""

    # Loop through the string in reverse order
    # 'range(len(string))' generates a sequence of indexes from 0 to the length of the string - 1.
    # 'reversed(range(len(string)))' will reverse this sequence, allowing us to loop from the last index to the first.
    for i in reversed(range(len(string))):
        # Append the character at the current index (i) to the reversedString
        reversedString += string[i]

    # Check if the original string is equal to the reversed string.
    # If they are the same, return True (the string is a palindrome), otherwise return False.
    return string == reversedString


# Second solution

def isPalindrome(string):
    """
    Understanding [::-1]
        start: Not specified (defaults to the beginning of the sequence).
        stop: Not specified (defaults to the end of the sequence).
        step: -1, which means to go through the sequence backwards.
    """
    return string == string[::-1]


# Solution 3 with append() method

def isPalindrome(string):
    # Write your code here.
    reversedChars = []

    for i in reversed(range(len(string))):

        reversedChars.append(string[i])

    return string == "".join(reversedChars)

# Solution 4 Recursive skill

def isPalindrome(string, i=0):
    # Calculate the index of the character from the end of the string
    j = len(string) - 1 - i

    # Base case: if 'i' is greater than or equal to 'j', all characters have been checked
    return True if i >= j else (
        # Check if the characters at positions 'i' and 'j' are equal
        # If they are equal, continue checking the next pair of characters
        string[i] == string[j] and isPalindrome(string, i + 1)
    )
def isPalindrome(string, i=0): # Recursive skill
    j = len(string) - 1 - i

    if i >= j:
        return True  # Base case: all characters have been checked
    if string[i] != string[j]:
        return False  # If characters at positions 'i' and 'j' are not equal, it's not a palindrome
    return isPalindrome(string, i + 1)  # Recursive call with incremented index

# BEST Solution

def isPalindrome(string):
    # Initialize two pointers: one at the start and one at the end of the string
    leftIdx = 0
    rightIdx = len(string) - 1

    # Continue checking characters while the left index is less than the right index
    while leftIdx < rightIdx:
        # If the characters at the current indices do not match, return False
        if string[leftIdx] != string[rightIdx]:
            return False

        # Move the left index forward (towards the center)
        leftIdx += 1
        # Move the right index backward (towards the center)
        rightIdx -= 1

    # If all characters matched, the string is a palindrome; return True
    return True


s = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert the string to lowercase and assign it back to 's'
        s = s.lower()

        # Create a new string that only contains alphanumeric characters
        new_string = "".join(char for char in s if char.isalnum())

        # Initialize two pointers, one at the beginning and one at the end
        leftIndex = 0
        rightIndex = len(new_string) - 1

        # Compare characters from both ends moving towards the center
        while leftIndex < rightIndex:
            if new_string[leftIndex] != new_string[rightIndex]:
                return False  # If characters don't match, it's not a palindrome
            rightIndex -= 1
            leftIndex += 1

        return True  # If all characters match, it is a palindrome
