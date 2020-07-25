class Solution:
    def splitArray(self, nums: list, m: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            count = 0
            sub_sum = 0
            for i in range(len(nums)):
                sub_sum += nums[i]
                if sub_sum > mid:
                    sub_sum = nums[i]
                    count += 1
            count += 1

            if count > m:
                low = mid + 1
            else:
                high = mid
        return low
