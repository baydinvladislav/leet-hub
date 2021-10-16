class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        possible_dups = arr.count(0)

        for i in range(n - 1, -1, -1):
            if i + possible_dups < n:
                arr[i + possible_dups] = arr[i]

            if arr[i] == 0:
                possible_dups -= 1

                if i + possible_dups < n:
                    arr[i + possible_dups] = 0

        print(arr)