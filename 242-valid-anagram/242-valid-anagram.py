class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_a, dict_b = {}, {}
        for char in s:
            dict_a[char] = dict_a.get(char, 0) + 1
        
        for char in t:
            dict_b[char] = dict_b.get(char, 0) + 1
        
        return dict_a == dict_b
