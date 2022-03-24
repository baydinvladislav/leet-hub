class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        return prev
