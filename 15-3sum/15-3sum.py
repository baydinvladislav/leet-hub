class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        if set(nums) == {0}:
            return [[0,0,0]]
        
        
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            self.search_pair(nums, triplets, left=i + 1, target_sum=-nums[i])
        return triplets

    def search_pair(self, arr, triplets, left, target_sum):
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                # skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif current_sum < target_sum:
                left += 1

            elif current_sum > target_sum:
                right -= 1
