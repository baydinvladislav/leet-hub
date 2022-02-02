# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def levelOrder(self, root):
            if not root:
                return []
            
            values = []
            queue = deque()
            queue.append(root)
            while queue:
                cur_level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    cur_level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                values.append(cur_level)

            return values