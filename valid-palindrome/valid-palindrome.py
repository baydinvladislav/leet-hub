class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_symbols = filter(lambda ch: ch.isalnum(), s)
        low_case = map(lambda ch: ch.lower(), filtered_symbols)
        result_list = list(low_case)
        return result_list == result_list[::-1]