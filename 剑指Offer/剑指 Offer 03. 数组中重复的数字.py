# 方法一： 先排序，然后看相邻元素是否有相同的，有直接return。 不过很慢，时间O(nlogn)了，空间O(1)

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]
# 方法二：哈希表 时间O(n)，空间O（n）

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}
        for num in nums:
            if num not in repeatDict:
                repeatDict[num] = 1
            else:
                return num
# 方法三：时间复杂度O(n)，空间复杂度O(1)。可以看做是一种原地哈希，不过没有用到字典。具体做法就是因为题目中给的元素是 < len（nums）的，所以我们可以让 位置i 的地方放元素i。如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该在的位置，即 nums[i] 和nums[nums[i]]的元素交换，这样就把原来在nums[i]的元素正确归位了。如果发现 要把 nums[i]正确归位的时候，发现nums[i]（这个nums[i]是下标）那个位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return

class Solution:
    def findRepeatNumber(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            #   注意这里不要写成nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            #   这种嵌套的直接交换在python里面得到的不是你想要的。提交了好几次发现之间在里面死循环了，debug了一下才发现有问题
if __name__ == '__main__':
    s = Solution()
    s.findRepeatNumber()