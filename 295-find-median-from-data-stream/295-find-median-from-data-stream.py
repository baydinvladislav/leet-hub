class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.len = len(self.store)
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # keep a sorted array
        # use binary search to find insertion index

        low = 0
        high = self.len - 1

        while low <= high:
            mid = (low + high) // 2
            if self.store[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1

        self.store.insert(low, num)
        self.len += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # as array is always sorted we can always use the same median property

        if self.len % 2 == 0:
            temp = self.len // 2
            return (self.store[temp] + self.store[temp - 1]) / 2.0
        else:
            return self.store[self.len // 2]
