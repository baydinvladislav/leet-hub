class Solution:
    # Iterative
    def reverseList(self, head):
        """
        1. temporarily store the next node
        2. reverse the current node
        3. before we move to the next node, point previous to the current node
        4. move on the next node
        """
        prev = None
        current = head
        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        return prev