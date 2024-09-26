def commonCharacters(strings):
    # 1. Create an empty dictionary
    charCounts = {}

    for string in strings:
        uniqueStringChars = set(string)  # Get unique characters from the current string
        for char in uniqueStringChars:
            if char not in charCounts:  # Check if character is already in the dictionary
                charCounts[char] = 0  # Initialize count for the character
            charCounts[char] += 1  # Increment the count for this character

    # 2. Final empty list
    finalChars = []
    for char, count in charCounts.items():
        if count == len(strings):  # Check if character appears in all strings
            finalChars.append(char)  # Add to final list if it does

    return finalChars  # Return the list of common characters
