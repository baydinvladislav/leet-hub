class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        buffer = {}
        shuffled_str = ''
        for i in range(len(s)):
            buffer[indices[i]] = s[i]

        for j in range(len(buffer)):
            shuffled_str += buffer[j]
        return shuffled_str


print(Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))