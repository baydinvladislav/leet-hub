class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for i in operations:
            if '+' in i:
                val += 1
            elif '-' in i:
                val -= 1
            else:
                print('Input is not correct')
        return val