# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value  # Initialize the node with a value.
        self.next = None  # Initialize the next pointer to None.


# Example linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4
def removeDuplicatesFromLinkedList(linkedList):
    # Start with the head of the list.
    currentNode = linkedList

    # Loop until we reach the end of the list.
    while currentNode is not None:
        # Set nextDistinctNode to the next node in the list.
        nextDistinctNode = currentNode.next

        # Loop to find the next distinct value.
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            # Move to the next node until we find a distinct value.
            nextDistinctNode = nextDistinctNode.next

        # At this point, nextDistinctNode points to the next distinct node or None.
        # Update the currentNode's next pointer to skip duplicates.
        currentNode.next = nextDistinctNode  # This is where we remove duplicates.

        # Move currentNode to the next distinct node for the next iteration.
        currentNode = nextDistinctNode

    return linkedList  # Return the modified linked list.


