class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        hash_map = {}

        window_start = 0
        for window_end in range(n):
            cur_char = s[window_end]
            if cur_char in hash_map:
                window_start = max(hash_map[cur_char], window_start)

            result = max(result, window_end - window_start + 1)
            hash_map[cur_char] = window_end + 1

        return result