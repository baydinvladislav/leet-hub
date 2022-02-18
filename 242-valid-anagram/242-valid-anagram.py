class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 , d2 = defaultdict(int), defaultdict(int)
        for key in s:
            d1[key] += 1
        
        for key in t:
            d2[key] += 1 
        
        return d1 == d2
            