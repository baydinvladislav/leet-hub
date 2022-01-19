class Solution:
    def productExceptSelf(self, nums):
        result = []

        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            result[i] *= postfix
            postfix *= nums[i]

        return result
        