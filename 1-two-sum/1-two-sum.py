class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        buffer = {}
        for i in range(len(nums)):
            buffer[nums[i]] = i
            
        for i in range(len(nums)):
            attempt = target - nums[i]
            if attempt in buffer and buffer[attempt] != i:
                return [i, buffer[attempt]]
        return [-1, -1]
            
        