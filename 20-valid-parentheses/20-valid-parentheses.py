class Solution:
    def isValid(self, s):
        hash_map = {'(': ')', '[': ']', '{': '}',}
        stack = deque()
        
        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                last_el = stack.pop()
                if hash_map[last_el] != char:
                    return False
        return not stack
                