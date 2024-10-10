def validWordAbbreviation(word: str, abbr: str) -> bool:

    # Time Complexity O(n+m)
    # Space O(1
    i, j = 0, 0  # Pointers for word and abbr
    n, m = len(word), len(abbr)

    while i < n and j < m:
        if abbr[j].isalpha():  # If the character in abbr is a letter
            if word[i] != abbr[j]:
                return False  # Mismatch found
            i += 1
            j += 1
        else:  # If the character in abbr is a digit
            start = j
            while j < m and abbr[j].isdigit():  # Read the full number
                j += 1

            num = int(abbr[start:j])  # Convert to integer

            # Check for leading zeroes (invalid if j-start > 1)
            if j - start > 1 and abbr[start] == '0':
                return False

            # Move the pointer i in the word forward by num
            i += num

            if i > n:  # If we've moved past the end of the word
                return False

    # Both pointers should be at the end of their strings
    return i == n and j == m
