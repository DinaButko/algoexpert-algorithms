# First Solution Time O(n^2) Space O(n)

def getNthFib(n):
     if n == 2:
         return 1
     elif n == 1:
         return 0

     else:
         return getNthFib(n-1) + getNthFib(n-2)


# Second Solution Time O(n), Space O(n)

def getNthFib(n, memory={1: 0, 2: 1}):
    # Write your code here.
    if n in memory:
        return memory[n]
    else:
        memory[n] = getNthFib(n-1, memory) + getNthFib(n-2, memory)
        return memory[n]

# Third Solution
# Second Solution Time O(n), Space O(1)
def getNthFib(n):
    # Write your code here.
    lastTwo = [0,1]
    counter = 3

    while counter <=n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]