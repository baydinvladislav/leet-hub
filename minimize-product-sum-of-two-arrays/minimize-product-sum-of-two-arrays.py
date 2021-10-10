class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1.sort()
        nums2.sort()
        j = n - 1
        sum = 0

        for i in range(n):
            comp = nums1[i] * nums2[j]
            sum += comp
            j -= 1

        return sum