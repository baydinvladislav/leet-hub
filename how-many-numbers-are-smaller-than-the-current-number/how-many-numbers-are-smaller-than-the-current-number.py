class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            counter = 0
            for j in nums:
                if i > j:
                    counter += 1
            else:
                res.append(counter)
        return res


print(Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))