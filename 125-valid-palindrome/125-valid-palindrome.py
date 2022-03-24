class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_symbols = filter(lambda symbol: symbol.isalnum(), s)
        lo_low_case = map(lambda symbol: symbol.lower(), filtered_symbols)
        to_list = list(lo_low_case)
        return to_list == to_list[::-1]