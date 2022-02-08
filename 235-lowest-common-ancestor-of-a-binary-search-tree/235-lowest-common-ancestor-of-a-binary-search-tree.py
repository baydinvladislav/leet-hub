class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            # Value of current node or parent node.
            parent_val = node.val

            if p.val > parent_val and q.val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p.val < parent_val and q.val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
