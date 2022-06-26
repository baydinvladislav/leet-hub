class Solution(object):
    def pathExist(self, row, col, word):
        if len(word) == 0:
            return True
    
        if row < 0 or col < 0 or row == self.rows or col == self.cols or self.board[row][col] != word[0]:
            return False

        self.board[row][col] = '$'
        result = False
        for rowOffset, colOffset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            result = self.pathExist(row + rowOffset, col + colOffset, word[1:])
            if result:
                break

        self.board[row][col] = word[0]
        return result
    
    def exist(self, board, word):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for i in range(self.rows):
            for j in range(self.cols):
                if self.pathExist(i, j, word):
                    return True
                
        return False