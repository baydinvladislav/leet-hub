class Solution:
        # iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
            
        return root