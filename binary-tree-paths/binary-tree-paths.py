class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]

        result = []
        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
                return
            dfs(root.left, path + '->')
            dfs(root.right, path + '->')

        dfs(root, "")
        return result