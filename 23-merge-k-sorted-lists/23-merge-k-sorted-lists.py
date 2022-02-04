class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:        
        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                heappush(q, (l.val, id(l), l))
        while q:
            val, nodeId, node = heappop(q)
            point.next = node # use node directly instead of creating a new node
            point = point.next
            node = node.next
            if node:
                heappush(q, (node.val, id(node), node))
        return head.next