class Solution:
        def lowestCommonAncestor(self, root, p, q):
            # If both p and q are greater than parent
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)

            # If both p and q are lesser than parent
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)

            # We have found the split point, i.e. the LCA node.
            else:
                return root