def runLengthEncoding(string):
    # Initialize a list to hold the encoded characters and their counts
    encodedStringChar = []
    # Set the initial run length to 1 for the first character
    currentRunLen = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(string)):
        # Current character being processed
        currentChar = string[i]
        # Previous character to compare with
        previousChar = string[i - 1]

        # Check if the current character is different from the previous one
        # or if the current run length has reached 9
        if currentChar != previousChar or currentRunLen == 9:
            # Append the current run length and the previous character to the list
            encodedStringChar.append(str(currentRunLen))  # Convert length to string
            encodedStringChar.append(str(previousChar))  # Convert character to string
            # Reset the run length counter
            currentRunLen = 0

        # Increment the run length for the current character
        currentRunLen += 1

        # After the loop, append the last run length and character to the list
    encodedStringChar.append(str(currentRunLen))  # Final run length
    encodedStringChar.append(string[len(string) - 1])  # Last character

    # Join the list into a single string and return it
    return "".join(encodedStringChar)
