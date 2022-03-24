class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.map:
            self._remove_node(self.map[key])

        node = Node(key, value)
        self._add_node(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            deleted_node = self.head.next
            self._remove_node(deleted_node)
            del self.map[deleted_node.key]

    def _add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
