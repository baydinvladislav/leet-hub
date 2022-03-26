class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        window_start = result = 0
        
        for window_end in range(len(s)):
            if s[window_end] in hash:
                window_start = max(window_start, hash[s[window_end]])
            
            result = max(result, window_end - window_start + 1)
            hash[s[window_end]] = window_end + 1
            
        return result