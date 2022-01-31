class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_freq = {}
        window_start = max_length = max_repeat = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in dict_freq:
                dict_freq[right_char] = 0
            dict_freq[right_char] += 1
            max_repeat = max(max_repeat, dict_freq[right_char])

            if k < window_end - window_start + 1 - max_repeat:
                dict_freq[s[window_start]] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length