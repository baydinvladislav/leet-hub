class Solution:
    # Iterative
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        return prev