class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 128
        start = end = result = 0
        
        while end < len(s):
            last_ch = s[end]
            char_idx = ord(last_ch)
            arr[char_idx] += 1
            
            while arr[ord(last_ch)] > 1:
                first_ch = s[start]
                char_idx = ord(first_ch)
                arr[char_idx] -= 1
                start += 1
            
            result = max(result, end - start + 1)
            end += 1
            
        return result
            
    
    
    
    
    
    
    
    
    
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
        
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if self.checker(i, j, s):
#                     length = j - i + 1
#                     max_length = max(length, max_length)
#         return max_length
    
#     def checker(self, start, end, s):
#         arr = [0] * 128
        
#         for i in range(start, end + 1):
#             arr[ord(s[i])] += 1
#             if arr[ord(s[i])] > 1:
#                 return False
#         return True