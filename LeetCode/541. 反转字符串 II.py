class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]
        l, r = 0, len(s) - 1
        ans = ""
        while l <= r:
            ans += s[l:l+k][::-1] + s[l+k:l+2*k]
            l += 2*k
        return ans
