class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        logic_arr = []

        for i in range(n):
            var = candies[i] + extraCandies
            if var >= max(candies):
                logic_arr.append(True)
            else:
                logic_arr.append(False)

        return logic_arr
        