class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        res = 0
        for number in nums:
            if number in hash_map:
                res += hash_map[number]
                hash_map[number] += 1
            else:
                hash_map[number] = 1
        return res