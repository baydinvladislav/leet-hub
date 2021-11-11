class Solution:
    def moveZeroes(self, nums):
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1