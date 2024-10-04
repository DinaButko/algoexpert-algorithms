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


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        words_size = len(words)
        result = []

        # Initialize common_character_counts with the characters from the first word
        common_character_counts = collections.Counter(words[0])

        for i in range(1, words_size):
            # Count characters in the current word
            current_character_counts = collections.Counter(words[i])

            # Update the common character counts to keep the minimum counts
            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter],
                )

        # Collect the common characters based on the final counts
        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result
