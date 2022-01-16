class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        buffer_1, buffer_2 = {}, {}

        for char in s:
            buffer_1[char] = buffer_1.get(char, 0) + 1

        for char in t:
            buffer_2[char] = buffer_2.get(char, 0) + 1

        return buffer_1 == buffer_2