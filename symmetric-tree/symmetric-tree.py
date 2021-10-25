class Solution:

    def _in_order_traversal_left(self, node, left_arr):
        if node is not None:
            self._in_order_traversal_left(node.left, left_arr)
            left_arr.append(node.val)
            self._in_order_traversal_left(node.right, left_arr)
        left_arr.append(None)

    def _in_order_traversal_right(self, node, right_arr):
        if node is not None:
            self._in_order_traversal_right(node.right, right_arr)
            right_arr.append(node.val)
            self._in_order_traversal_right(node.left, right_arr)
        right_arr.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        self._in_order_traversal_left(root.left, left)
        self._in_order_traversal_right(root.right, right)

        if left == right:
            return True
        else:
            return False