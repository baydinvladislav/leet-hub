class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result_1 = []
        result_2 = []

        def dfs(node, result_arr):
            if not node:
                return

            dfs(node.left, result_arr)
            result_arr.append(node.val)
            dfs(node.right, result_arr)

        dfs(root1, result_1)
        dfs(root2, result_2)

        result_1.extend(result_2)
        result_1.sort()
        return result_1