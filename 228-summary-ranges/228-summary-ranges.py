class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = end = 0
        result = []
        while end < len(nums):
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1
            
            if nums[start] != nums[end]:
                result.append(f'{nums[start]}->{nums[end]}')
            else:
                result.append(f'{nums[start]}')
            
            end += 1
            start = end
            
        return result
    