class Solution:

    def traversal_left_tree(self, node, values_arr):

        if node is None:
            return

        self.traversal_left_tree(node.left, values_arr)
        values_arr.append(node.val)
        self.traversal_left_tree(node.right, values_arr)

        values_arr.append(None)

    def traversal_right_tree(self, node, values_arr):

        if node is None:
            return

        self.traversal_right_tree(node.right, values_arr)
        values_arr.append(node.val)
        self.traversal_right_tree(node.left, values_arr)

        values_arr.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        self.traversal_left_tree(root.left, left)
        self.traversal_right_tree(root.right, right)

        return left == right