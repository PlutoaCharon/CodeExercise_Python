from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        dct1 = defaultdict(int)
        dct2 = defaultdict(int)
        for i in nums1:
            dct1[i] += 1
        for i in nums2:
            dct2[i] += 1
        dct3 = {i: min(dct1[i], dct2[i]) for i in set(dct1) & set(dct2)}
        return sum([[key] * val for key, val in dct3.items()], [])
