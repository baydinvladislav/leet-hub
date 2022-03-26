class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 128
        result = start = end = 0
        
        while end < len(s):
            last_symbol = s[end]
            index = ord(last_symbol)
            arr[index] += 1
            
            while arr[ord(last_symbol)] > 1:
                first_symbol = s[start]
                index = ord(first_symbol)
                arr[index] -= 1
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
    