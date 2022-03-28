class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        matched = 0
        hash_map = {}
        
        for ch in s1:
            if ch not in hash_map:
                hash_map[ch] = 0
            hash_map[ch] += 1
            
        for window_end in range(len(s2)):
            last_symbol = s2[window_end]
            if last_symbol in hash_map:
                hash_map[last_symbol] -= 1
                if hash_map[last_symbol] == 0:
                    matched += 1
            
            if matched == len(hash_map):
                return True
            
            if window_end >= len(s1) - 1:
                left_symbol = s2[window_start]
                if left_symbol in hash_map:
                    if hash_map[left_symbol] == 0:
                        matched -= 1
                    hash_map[left_symbol] += 1
                window_start += 1
        return False
