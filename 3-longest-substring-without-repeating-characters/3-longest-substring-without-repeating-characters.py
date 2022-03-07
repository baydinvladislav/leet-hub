class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_array = [0] * 128
        window_start = window_end = 0
        result = 0
        while window_end < len(s):
            last_symbol = s[window_end]
            symbol_unicode = ord(last_symbol)
            ascii_array[symbol_unicode] += 1

            while ascii_array[ord(last_symbol)] > 1:
                first_symbol = s[window_start]
                symbol_unicode = ord(first_symbol)
                ascii_array[symbol_unicode] -= 1
                window_start += 1

            result = max(result, window_end - window_start + 1)
            window_end += 1
        return result