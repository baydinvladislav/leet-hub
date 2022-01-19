class Solution:
    def maxProduct(self, nums):
        answer = nums[0]
        product = 0
        for i in range(len(nums)):
            if product == 0:
                product = nums[i]
            else:
                product *= nums[i]
            answer = max(answer, product)

        product = 0
        for i in range(len(nums) - 1, -1, -1):
            if product == 0:
                product = nums[i]
            else:
                product *= nums[i]
            answer = max(answer, product)
        return answer