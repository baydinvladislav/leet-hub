class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_arr = nums[:n]
        y_arr = nums[n:]

        res = []
        i = 0
        while i < len(x_arr):
            res.append(x_arr[i])
            res.append(y_arr[i])
            i += 1

        return res


print(Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))