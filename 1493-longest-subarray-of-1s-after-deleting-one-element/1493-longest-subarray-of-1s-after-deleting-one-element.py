class Solution:
        def longestSubarray(self, nums: List[int]) -> int:
            start = ones = max_length = 0
            
            for end in range(len(nums)):
                if nums[end] == 1:
                    ones += 1
                    
                if end - start + 1 - ones > 1:
                    if nums[start] == 1:
                        ones -= 1
                    start += 1
                
                max_length = max(max_length, end - start)
            return max_length