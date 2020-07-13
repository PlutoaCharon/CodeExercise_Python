class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 排序 时间复杂度（nlogn + mlogm)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        # 长度
        l1, l2 = len(nums1), len(nums2)
        # 定义双指针
        index1, index2 = 0, 0
        ans = []
        while index1 < l1 and index2 < l2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                ans.append(nums1[index1])
                index1 += 1
                index2 += 1
        return ans


from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct1 = defaultdict(int)
        for i in nums1:
            dct1[i] += 1
        dct2 = defaultdict(int)
        for i in nums2:
            dct2[i] += 1
        dct3 = {i: min(dct1[i], dct2[i]) for i in set(dct1) & set(dct2)}
        return sum([[key] * val for key, val in dct3.items()], [])
