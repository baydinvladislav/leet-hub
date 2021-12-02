class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window_start, max_length, ones = 0, 0, 0
        
        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                ones += 1
            
            if window_end - window_start + 1 - ones > 1:
                if nums[window_start] == 1:
                    ones -= 1
                window_start += 1
                
            max_length = max(max_length, window_end - window_start )
                
        return max_length