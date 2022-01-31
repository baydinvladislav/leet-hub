class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length, max_repeat = 0, 0, 0
        dict_index = {}

        for window_end in range(len(s)):
            if s[window_end] not in dict_index:
                dict_index[s[window_end]] = 0
            dict_index[s[window_end]] += 1
            max_repeat = max(max_repeat, dict_index[s[window_end]])

            if k < window_end - window_start + 1 - max_repeat:
                dict_index[s[window_start]] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length
