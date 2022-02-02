class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        buffer = {}
        for i in range(len(nums)):
            if nums[i] not in buffer:
                buffer[nums[i]] = i
            else:
                return True
        return False
        