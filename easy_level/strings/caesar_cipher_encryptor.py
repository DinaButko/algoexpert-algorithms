def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
    newKey = key % 26 #This line ensures that the key is within the range of the alphabet (0-25). For example, a key of 27 is effectively the same as a key of 1.

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))

    return "".join(newLetters)


def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key # This finds the index of the current letter in the alphabet and adds the shift (key) to it.
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[newLetterCode % 26]


#Alernative method

def getNewLetter(letter, key, alphabet):
    # Find the current index of the letter in the alphabet
    currentIndex = alphabet.index(letter)

    # Calculate the new index with wrapping
    newIndex = (currentIndex + key) % 26

    # Return the letter at the new index
    return alphabet[newIndex]


def caesarCipherEncryptor(string, key):
    """
    Encrypts a given string using the Caesar cipher with a specified key.

    Args:
        string (str): The input string to encrypt.
        key (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted string.
    """
    new_letters = []  # List to hold the encrypted letters

    new_key = key % 26  # Normalize the key to be within the range of 0-25

    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet

    # Loop through each letter in the input string
    for letter in string:
        # Append the encrypted letter to the new_letters list
        new_letters.append(calculate_new_letter(letter=letter, key=new_key, alphabet=alphabet))

    return "".join(new_letters)  # Join the list into a single string and return


def calculate_new_letter(letter, key, alphabet):
    """
    Calculates the new letter after shifting it by the key in the alphabet.

    Args:
        letter (str): The letter to shift.
        key (int): The number of positions to shift the letter.
        alphabet (str): The string representing the alphabet.

    Returns:
        str: The new letter after applying the shift.
    """
    current_index = alphabet.index(letter)  # Find the current index of the letter
    new_index = (current_index + key) % 26  # Calculate the new index, wrapping around if necessary
    return alphabet[new_index]  # Return the letter at the new index
