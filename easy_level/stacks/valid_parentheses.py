class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time and O(n) space complexity (n - len of string)
        stack = []  # Initialize an empty stack
        mapping = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else ''  # Pop from stack if not empty
                if mapping[char] != top_element:  # Check for matching
                    return False
            else:  # If it's an opening bracket
                stack.append(char)  # Push onto stack

        return not stack  # If stack is empty, return True; otherwise, return False