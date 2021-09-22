class Solution:
    def firstUniqChar(self, s: str) -> int:
        storage = {}
        n = len(s)

        for i in range(n):
            if s[i] in storage:
                storage[s[i]] += 1
            else:
                storage[s[i]] = 1

        for key in storage.keys():
            if storage[key] == 1:
                return s.index(key)
        else:
            return -1
        