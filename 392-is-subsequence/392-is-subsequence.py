class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        while True:
            if left == len(s):
                return True
            if right == len(t):
                return False

            if s[left] == t[right]:
                left += 1
            right += 1
