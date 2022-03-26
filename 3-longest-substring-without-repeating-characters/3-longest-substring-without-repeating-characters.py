class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] *  128
        start = end = result = 0
        
        while end < len(s):
            arr[ord(s[end])] += 1
            
            while arr[ord(s[end])] > 1:
                arr[ord(s[start])] -= 1
                start += 1
            
            result = max(result, end - start + 1)
            end += 1
            
        return result
