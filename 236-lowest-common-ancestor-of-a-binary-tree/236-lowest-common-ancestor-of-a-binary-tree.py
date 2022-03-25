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
            
            left = recursive(node.left)
            right = recursive(node.right)
            mid = node.val == p.val or node.val == q.val
            
            if left + right + mid >= 2:
                self.result = node
            
            return left or right or mid
        
        recursive(root)
        return self.result
            
            