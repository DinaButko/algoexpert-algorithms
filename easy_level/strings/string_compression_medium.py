class Solution:
    def compress(self, chars: List[str]) -> int:

        #Time complexity O(n)
        # Space complexity O(n)
        finalArray = []
        countChar = 1

        for i in range(1, len(chars)):
            currentChar = chars[i]
            previousChar = chars[i-1]

            if currentChar != previousChar:
                finalArray.append(previousChar)

                if countChar > 1:
                    finalArray.extend(list(str(countChar)))

                countChar = 1
            else:
                countChar += 1

        # work on last elements

        finalArray.append(chars[-1])
        if countChar > 1:
            finalArray.extend(list(str(countChar)))

        chars[:len(finalArray)] = finalArray
        return len(finalArray)