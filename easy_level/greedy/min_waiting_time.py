def minimumWaitingTime(queries):
    # Write your code here.

    # Sort array
    queries.sort()

    totalWaitingTime = 0

    for index, duration in enumerate(queries):
        queriesLeft = len(queries) - (index + 1)
        totalWaitingTime += duration*queriesLeft
    return totalWaitingTime