class Solution(object):
    def groupAnagrams(self, strs):
        char_map = collections.defaultdict(list)
        for word in strs:
            sorted_chars = sorted(word)
            key = tuple(sorted_chars)
            char_map[key].append(word)
        return char_map.values()
        