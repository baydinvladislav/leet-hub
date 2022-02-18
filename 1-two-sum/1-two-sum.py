class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, num in enumerate(nums):
            hash_map[num] = i
        
        for i, num in enumerate(nums):
            attempt = target - num
            if attempt in hash_map and hash_map[attempt] != i:
                return [i, hash_map[attempt]]
        return [-1, -1]
        
                
        