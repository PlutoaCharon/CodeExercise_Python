class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.strip().split()[::-1])
        if not s:
            return ""
        s = s.strip()
        res = []
        i = j = len(s) - 1
        while i >= 0 :
            while i >= 0 and s[i] != " ": i -= 1
            res.append(s[i+1:j+1])
            while s[i] == " ": i -= 1
            j = i
        return " ".join(res)