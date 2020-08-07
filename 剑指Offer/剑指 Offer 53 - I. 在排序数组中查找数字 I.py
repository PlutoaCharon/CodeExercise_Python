class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return 0

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
                    # True 查找左边界 False查找右边界
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

        n = len(nums)
        return find(False) - find(True) + 1 if find(False) != -1 and find(True) != -1 else 0
