class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window_start = 0
        result = float('-inf')
        hash_map = {}
        
        for window_end in range(len(s)):
            if s[window_end] not in hash_map:
                hash_map[s[window_end]] = 0
            hash_map[s[window_end]] += 1
            
            while len(hash_map) > 2:
                hash_map[s[window_start]] -= 1
                if hash_map[s[window_start]] == 0:
                    del hash_map[s[window_start]]
                window_start += 1
            result = max(result, window_end - window_start + 1)
        return result
