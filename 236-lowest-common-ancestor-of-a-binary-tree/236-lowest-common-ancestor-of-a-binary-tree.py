# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursive(node):
            if not node:
                return False
            
            left_branch = recursive(node.left)
            right_branch = recursive(node.right)
            middle = node.val == p.val or node.val == q.val
            
            if left_branch + right_branch + middle >= 2:
                self.result = node
            
            return left_branch or right_branch or middle
        
        recursive(root)
        return self.result
    