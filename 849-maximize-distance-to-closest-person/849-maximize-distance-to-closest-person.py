class Solution:
    def maxDistToClosest(self, seats):
        reserved = (i for i, seat in enumerate(seats) if seat == 1)
        prev, future = None, next(reserved)
        result = 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(reserved, None)
                
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                result = max(result, min(left, right))
        
        return result