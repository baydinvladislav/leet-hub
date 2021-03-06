class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for word in strs:
            hash_map[tuple(sorted(word))].append(word)
        return list(hash_map.values())
