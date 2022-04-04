class HitCounter:

    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp] = 0
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300
        count = 0
        for i in range(begin + 1, timestamp + 1):
            if i in self.hits:
                count += self.hits[i]
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)