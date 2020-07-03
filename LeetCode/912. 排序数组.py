# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  -50000 <= nums[i] <= 50000
#
#  👍 144 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return self.quick_sort(nums, 0, len(nums) - 1)
        return self.quick_sort(nums)

    '''    
    def quick_sort(self, nums, left, right):
        if left > right:
            return 

        if left < right:
            mid = self.partition(nums, left, right)
            self.quick_sort(nums, left, mid-1)
            self.quick_sort(nums, mid+1, right)
        return nums

    def partition(self, nums, left, right):
        tmp = nums[left]
        while left < right:
            while left < right and nums[right] >= tmp:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= tmp:
                left += 1
            nums[right] = nums[left]
        nums[left] = tmp
        return left
    '''

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums
        tmp = nums[0]
        left = [i for i in nums[1:] if i <= tmp]
        right = [i for i in nums[1:] if i > tmp]
        left = self.quick_sort(left)
        right = self.quick_sort(right)

        return left + [tmp] + right