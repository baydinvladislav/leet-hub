class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        matched = 0
        hash = {}
        
        for char in s1:
            if char not in hash:
                hash[char] = 0
            hash[char] += 1
        
        for window_end in range(len(s2)):
            last_symbol = s2[window_end]
            if last_symbol in hash:
                hash[last_symbol] -= 1
                if hash[last_symbol] == 0:
                    matched += 1
            
            if matched == len(hash):
                return True
            
            if window_end >= len(s1) - 1:
                first_symbol = s2[window_start]
                if first_symbol in hash:
                    if hash[first_symbol] == 0:
                        matched -= 1
                    hash[first_symbol] += 1
                window_start += 1
                
        return False