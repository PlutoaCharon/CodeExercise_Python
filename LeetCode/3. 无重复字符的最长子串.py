class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start, res, dic = 0, 0, {}
        for i, value in enumerate(s):
            if value in dic and dic[value] >= start:
                start = dic[value] + 1
                dic[value] = i
            else:
                dic[value] = i
                cur = i - start + 1
                res = max(cur, res)
        return res
