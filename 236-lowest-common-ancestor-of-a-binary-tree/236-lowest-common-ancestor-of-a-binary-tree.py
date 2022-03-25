class Solution:
    def __init__(self):
        self.answer = None

    def lowestCommonAncestor(self, root, p, q):
        def recursive(node):
        
            if not node:
                return False

            left_branch = recursive(node.left)
            right_branch = recursive(node.right)
            
            middle = node.val == p.val or node.val == q.val
            
            if int(left_branch) + int(right_branch) + middle >= 2:
                self.answer = node
            
            return left_branch or right_branch or middle
        
        recursive(root)   
        return self.answer
            