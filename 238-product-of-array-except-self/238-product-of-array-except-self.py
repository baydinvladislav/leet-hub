class Solution:
    def productExceptSelf(self, nums):
        answer = []
        
        prefix = 1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
        