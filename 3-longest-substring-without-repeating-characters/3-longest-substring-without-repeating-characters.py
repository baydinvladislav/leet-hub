class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        hash_map = {}

        i = 0
        for j in range(n):
            cur_char = s[j]
            if cur_char in hash_map:
                i = max(hash_map[cur_char], i)

            result = max(result, j - i + 1)
            hash_map[cur_char] = j + 1

        return result