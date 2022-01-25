class Solution:
    def maxSubArray(self, nums):
        current_subarray, max_subarray = float('-inf'), float('-inf')
        for num in nums:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray