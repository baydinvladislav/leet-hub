class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = OrderedDict()

    def get(self, key):
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.storage:
            self.storage.move_to_end(key)
        self.storage[key] = value

        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)