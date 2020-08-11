class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        # 排序 +　异或
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] ^ nums[i] == 0:
                return nums[i]
        return 0