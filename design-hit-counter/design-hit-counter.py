class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.hits:
            self.hits[timestamp] = 0
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        begin = timestamp - 300
        hits_for_ts = 0
        for i in range(begin + 1, timestamp + 1):
            if i in self.hits:
                hits_for_ts += self.hits[i]
        return hits_for_ts