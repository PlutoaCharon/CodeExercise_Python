class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0]

        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] > n // 2:
                    return i
        return None
