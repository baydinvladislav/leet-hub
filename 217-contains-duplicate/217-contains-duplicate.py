class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        buffer = {}
        for i in range(len(nums)):
            if nums[i] in buffer:
                return True
            buffer[nums[i]] = i
        return False
        