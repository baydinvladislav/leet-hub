class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0

        else:
            depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
            return 1 + depth