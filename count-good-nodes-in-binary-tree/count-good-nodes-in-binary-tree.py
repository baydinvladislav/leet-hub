class Solution:

    def tree_traversal(self, node, cur_max, good_nodes):

        if node is None:
            return

        if node.val >= cur_max:
            good_nodes[0] = good_nodes[0] + 1

        cur_max = max(cur_max, node.val)

        if node.left:
            self.tree_traversal(node.left, cur_max, good_nodes)

        if node.right:
            self.tree_traversal(node.right, cur_max, good_nodes)

    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1    
        
        good_nodes = [0]
        self.tree_traversal(root, root.val, good_nodes)

        return good_nodes[0]