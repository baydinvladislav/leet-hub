class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = list(s)
        t = list(t)
        
        s.sort()
        t.sort()
       
        i, j = 0, 0 
        while i != len(s):
            if s[i] != t[j]:
                return False
            i += 1 
            j += 1
        return True
            
        