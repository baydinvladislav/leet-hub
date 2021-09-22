class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        for i in range(n):
            for j in range(n):
                if nums[i] - nums[j] == k:
                    pairs += 1
        return pairs
        