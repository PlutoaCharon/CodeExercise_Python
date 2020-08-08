class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res, dic = 0, 0, {}
        for key, value in enumerate(s):
            # 如果字符出现过，并且大于start的值
            # 则从之前重复字符+1开始重新计算
            # 并且更新value值
            if value in dic and dic[value] >= start:
                start = dic[value] + 1
                dic[value] = key
            else:
            # 如果没有出现过或者出现过的value值小于start
                dic[value] = key
                tmp = key - start + 1
                res = max(res, tmp)
        return res