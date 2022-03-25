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
            middle = p.val == node.val or q.val == node.val
            
            if int(left_branch) + int(right_branch) + int(middle) >= 2:
                self.result = node
            
            return left_branch or right_branch or middle
            
        recursive(root)
        return self.result