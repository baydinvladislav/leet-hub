class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        hash = {}
        
        for end in range(len(s)):
            if s[end] in hash:
                start = max(start, hash[s[end]])
            
            result = max(result, end - start + 1)
            hash[s[end]] = end + 1
            
        return result