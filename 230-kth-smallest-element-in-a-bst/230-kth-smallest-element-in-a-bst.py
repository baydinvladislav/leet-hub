class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, values):
            if not node:
                return

            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

        values = []
        dfs(root, values)
        return values[k - 1]