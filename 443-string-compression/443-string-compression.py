class Solution:
    def compress(self, chars: List[str]) -> int:
        left = result = 0
        
        while left < len(chars):
            right = left
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
                
            chars[result] = chars[left]
            result += 1
            diff = right - left
            if diff > 1:
                for number in str(diff):
                    chars[result] = number
                    result += 1
            
            left = right
        return result
