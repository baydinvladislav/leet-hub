class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            hash_map[sorted_word].append(word)
        return hash_map.values()