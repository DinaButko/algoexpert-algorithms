def generateDocument(characters, document):
    # Write your code here.

    # Generate hash table
    charCounts = {}

    for char in characters:
        if char not in charCounts:
            charCounts[char] = 0
        charCounts[char]+=1

    for char in document:
        if char not in charCounts or charCounts[char]==0:
            return False

        charCounts[char] -= 1

    return True
