class Solution:
    def findTarget(self, root, k):
        if not root:
            return False

        queue, visited = [root], set()
        for node in queue:
            if k - node.val in visited:
                return True

            visited.add(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False