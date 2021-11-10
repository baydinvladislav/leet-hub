class Solution:

    def dfs(self, node, values):
        if not node:
            return

        self.dfs(node.left, values)
        values.append(node.val)
        self.dfs(node.right, values)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.dfs(root, values)

        i = 0
        j = 1
        
        while j != len(values):
            if values[i] >= values[j]:
                return False

            i += 1
            j += 1

        return True