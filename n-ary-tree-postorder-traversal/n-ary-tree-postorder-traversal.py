class Solution:
    # Recursive solution
    def dfs(self, root, visited):
        if root not in visited:
            for children in root.children:
                self.dfs(children, visited)
            visited.append(root)

    def postorder(self, root):
        if not root:
            return []
        visited = list()
        self.dfs(root, visited)
        sol = [x.val for x in visited]
        return sol