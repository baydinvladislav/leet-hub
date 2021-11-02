class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if root.left is None and root.right is None:
            return [root.val]

        def dfs(node, arr):
            if not node:
                return

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        values = []
        dfs(root, values)

        hash_map = {}
        for i in range(len(values)):
            if values[i] in hash_map:
                hash_map[values[i]] += 1
            else:
                hash_map[values[i]] = 1

        max_value = float('-inf')
        for key in hash_map.keys():
            if hash_map[key] > max_value:
                max_value = hash_map[key]

        result = []
        for key in hash_map.keys():
            if hash_map[key] == max_value:
                result.append(key)

        return result