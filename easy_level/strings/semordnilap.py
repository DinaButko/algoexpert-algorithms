def semordnilap(words):
    # Convert words to a set
    words_set = set(words)

    # Create a new array for pairs
    pairs_array = []

    for word in words:
        reverse = word[::-1]

        # Check if the reverse is in the set and not the same word
        if reverse in words_set and reverse != word:
            pairs_array.append([word, reverse])  # Use parentheses for append
            words_set.remove(word)
            words_set.remove(reverse)

    return pairs_array
