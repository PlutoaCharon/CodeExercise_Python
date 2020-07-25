class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return
        s = list(sorted(s))
        res = []

        def helper(s, tmp):
            if not s: res.append(''.join(tmp))
            for i, char in enumerate(s):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                helper(s[:i] + s[i + 1:], tmp + [char])

        helper(s, [])
        return res
