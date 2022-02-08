class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(root,subroot):
            
            #if both are none
            if not root and not subroot:
                return True
            
            
            #if any one is none
            if not root or not subroot:
                return False
            
            # if node value is not same
            if root.val!=subroot.val:
                return False
            
            #node vaule is same and check of left and right part of subtree
            return dfs(root.left,subroot.left) and dfs(root.right,subroot.right)
        
        def solve(root,subroot):
            
            #if tree is empty return false
            if not root:
                return False
            
            #check if subtree exist in tree or not with root node same for both
            if dfs(root,subroot):
                return True
            
            #check of subtree in right and left subtree of tree
            return solve(root.left,subroot) or solve(root.right,subroot)
        return solve(root,subRoot)