class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()[:k]
        return ' '.join(arr)