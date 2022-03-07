class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_array = [0] * 128
        left = right = 0

        result = 0
        while right < len(s):
            last_character = s[right]
            index = ord(last_character)
            ascii_array[index] += 1

            while ascii_array[ord(last_character)] > 1:
                first_character = s[left]
                index = ord(first_character)
                ascii_array[index] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1
        return result