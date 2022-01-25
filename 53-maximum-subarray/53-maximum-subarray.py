class Solution:
    def maxSubArray(self, nums):
        current_subarray = max_subarray = nums[0]

        for i in range(1, len(nums)):
            current_subarray = max(nums[i], current_subarray + nums[i])
            max_subarray = max(current_subarray, max_subarray)

        return max_subarray