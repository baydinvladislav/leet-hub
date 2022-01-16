class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        buffer = {}
        for num in nums:
            if num not in buffer:
                buffer[num] = 1
            else:
                return True
        return False
        