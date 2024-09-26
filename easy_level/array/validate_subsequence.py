"""
Validate Subsequence

Purpose The function isValidSubsequence(array, sequence) checks if sequence is a subsequence of array. A subsequence
means that the elements of sequence appear in array in the same order, but not necessarily consecutively."""

# Fist Solution

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    # Write your code here.
    arrIdx = 0
    seqIdx = 0

    for value in array:

        if arrIdx == len(sequence):
            return True

        if sequence[seqIdx] == value:
            arrIdx += 1

    return arrIdx == len(sequence)


# Second Solution

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence_second(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)


def isSubsequence_leetcode(s: str, t: str) -> bool:
    sSubIdx = 0
    tIdx = 0

    while sSubIdx < len(s) and tIdx < len(t):
        if s[sSubIdx] == t[tIdx]:
            sSubIdx += 1
        tIdx += 1

    return sSubIdx == len(s)


print(isSubsequence_leetcode(s="abc", t="ahbgdc"))


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sSubIdx = 0

        # If s is empty, it's a subsequence of any string
        # "If the string s is empty, return True because an empty string is always a subsequence."
        if not s:
            return True

        for value in t:
            # If we've matched all characters of s, we return True
            if sSubIdx == len(s):
                return True
            # Compare the current character in t with the current character in s
            if s[sSubIdx] == value:
                sSubIdx += 1

        # After looping, if sSubIdx matches the length of s, return True
        return sSubIdx == len(s)


def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0

    for value in array:

        if seqIdx == len(sequence):
            return True

        if value == sequence[seqIdx]:
            seqIdx += 1

    return seqIdx == len(sequence)