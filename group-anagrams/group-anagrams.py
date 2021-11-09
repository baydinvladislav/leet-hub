class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for word in strs:
            ans[tuple(sorted(word))].append(word)
        return ans.values()
        