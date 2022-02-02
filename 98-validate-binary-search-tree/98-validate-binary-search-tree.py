# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def isValidBST(self, root):
            if not root:
                return True

            queue = deque([(root, float('-inf'), float('inf'))])
            while queue:
                root, lower, upper = queue.popleft()

                if not root:
                    continue

                val = root.val
                if val <= lower or val >= upper:
                    return False

                queue.append((root.right, val, upper))
                queue.append((root.left, lower, val))
            return True

