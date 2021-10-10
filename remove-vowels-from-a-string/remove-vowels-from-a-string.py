class Solution:
    def removeVowels(self, s: str) -> str:
        n = len(s)
        new_str = ''

        for i in range(n):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                continue
            else:
                new_str += s[i]
        return new_str
