class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), -1, -1):
            for index in range(0, len(s) - length + 1):
                sub_string = s[index:length + index]
                if sub_string == sub_string[::-1]:
                    return sub_string
