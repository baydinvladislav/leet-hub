class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node('#', '#')
        self.tail = Node('#', '#')
        self.head.next = self.tail
        self.tail.prev = self.head

    # O(1)
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove_from_llist(node)
            self._add_to_llist(node)
            return node.value
        return -1

    # O(1)
    def put(self, key, value):
        if key in self.map:
            self._remove_from_llist(self.map[key])

        node = Node(key, value)
        self._add_to_llist(node)
        self.map[key] = node
        if len(self.map) > self.capacity:
            node = self.head.next
            self._remove_from_llist(node)
            del self.map[node.key]

    def _add_to_llist(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove_from_llist(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
