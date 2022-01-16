class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        buffer = {}
        for i, num in enumerate(nums):
            attempt = target - num
            if attempt not in buffer:
                buffer[num] = i
            else:
                return [buffer[attempt], i]

        return [-1, -1]