class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        '''
        # 先排序，双指针 超时
        nums1.sort()
        nums2.sort()

        i, j, ans = 0, 0, []
        while i <= len(nums1) and j <= len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1 
        return ans
        '''
        ans = []
        for i in nums1:
            if i in nums2 and i not in ans:
                ans.append(i)
        return ans
