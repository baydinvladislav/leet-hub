class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                print(other[i])
                if other[i] != ch:
                    return shortest[:i]

        return shortest