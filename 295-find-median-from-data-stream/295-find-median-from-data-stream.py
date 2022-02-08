class MedianFinder:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        low = 0
        high = len(self.store) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.store[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1

        self.store.insert(low, num)

    def findMedian(self):
        if len(self.store) % 2 == 0:
            temp = len(self.store) // 2
            return (self.store[temp] + self.store[temp - 1]) / 2.0
        else:
            return self.store[len(self.store) // 2]
