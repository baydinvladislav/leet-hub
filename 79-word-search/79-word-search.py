class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index):
            if index == len(word):
                return True
            
            if (not 0 <= x < len(board) or 
                not 0 <= y < len(board[0]) or 
                board[x][y] == '#' or 
                board[x][y] != word[index]):
                return False
            
            curr_letter = board[x][y]
            board[x][y] = '#'
            
            top = dfs(x - 1, y, index + 1)
            bottom = dfs(x + 1, y, index + 1)
            left = dfs(x, y - 1, index + 1)
            right = dfs(x, y + 1, index + 1)
            
            board[x][y] = curr_letter
            
            return top or bottom or left or right
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
