class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    # Time O(m+n)
    # Space O(1) we don't use additional memry 
    pointerA, pointerB = headA, headB

    # Traverse through both lists
    while pointerA != pointerB:
        # If pointerA reaches the end of list A, start from the beginning of list B
        pointerA = pointerA.next if pointerA else headB
        # If pointerB reaches the end of list B, start from the beginning of list A
        pointerB = pointerB.next if pointerB else headA

    # Either they meet at the intersection or at the end (both None)
    return pointerA
