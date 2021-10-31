class Solution:
    def bitwiseComplement(self, n: int) -> int:
        result = ''
        for ch in bin(n)[2:]:
            if ch == '0':
                result += '1'

            elif ch == '1':
                result += '0'

        return int(result, base=2)