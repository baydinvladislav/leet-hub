class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = 0

        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    jew += 1

        return jew