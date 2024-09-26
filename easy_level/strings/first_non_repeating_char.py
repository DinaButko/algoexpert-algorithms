def firstNonRepeatingCharacter(string):
    # Write your code here.

    calc_chars = {}

    for letter in string:
        calc_chars[letter] = calc_chars.get(letter, 0) + 1

    for index in range(len(string)):

        char = string[index]
        if calc_chars[char] == 1:
            return index

    return - 1