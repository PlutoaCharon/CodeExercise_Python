class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        n = len(nums)

        # 查找第一个和最后一个元素
        def find(is_find_first):
            begin = 0
            end = n - 1
            # if和elif的逻辑跟正常的二分查找一样
            while begin <= end:
                mid = begin + (end - begin) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    begin = mid + 1
                # 找到目标值了，开始定位到第一个和最后一个位置
                else:
                    # 查找第一个和最后一个逻辑很类似，这里用一个变量标记
                    # 是查找第一个还是查找最后一个
                    if is_find_first:
                        # 如果不满足条件，缩小右边界，继续往左边查找
                        if mid > 0 and nums[mid] == nums[mid - 1]:
                            end = mid - 1
                        else:
                            return mid
                    else:
                        # 如果不满足条件，增大左边界，继续往右边查找
                        if mid < n - 1 and nums[mid] == nums[mid + 1]:
                            begin = mid + 1
                        else:
                            return mid
            return -1

        return [find(True), find(False)]


# 第二种方法：
'''
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/duo-tu-yan-shi-34-zai-pai-xu-shu-zu-zhong-cha-zhao/

'''
