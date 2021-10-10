class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        n = len(vec.v)
        j = 0
        sum = 0
        for i in range(n):
            comp = self.v[i] * vec.v[j]
            sum += comp
            j += 1
        return sum