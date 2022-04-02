class Solution:
    def maxDistToClosest(self, seats):
        # about generator
        reserved = (i for i, seat in enumerate(seats) if seat == 1)
        prev = None
        future = next(reserved)
        result = 0
        
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(reserved, None)
                
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                result = max(result, min(left, right))
                
        return result
