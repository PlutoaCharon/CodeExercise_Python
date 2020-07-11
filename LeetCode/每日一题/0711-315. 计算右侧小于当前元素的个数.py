import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sort_nums = []
        ans = []
        for i in nums[::-1]:
            index = bisect.bisect_left(sort_nums, i)
            bisect.insort(sort_nums, i)
            ans.append(index)
        return ans[::-1]