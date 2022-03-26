class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = result = 0
        
        for end in range(len(s)):
            if s[end] in map:
                start = max(start, map[s[end]])
            
            result = max(result, end - start + 1)
            map[s[end]] = end + 1
            
        return result