class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(str(n))
        product = 1
        sum = 0

        for val in l:
            product *= int(val)
            sum += int(val)

        return product - sum