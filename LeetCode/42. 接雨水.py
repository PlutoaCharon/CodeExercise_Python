class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        n = len(height)
        for i in range(n):
            if max1 < height[i]:
                max1 = height[i]
            if max2 < height[n - i - 1]:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        ans = s1 + s2 - len(height) * max1 - sum(height)
        return ans