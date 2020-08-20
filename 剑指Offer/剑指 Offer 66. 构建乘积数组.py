class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        L, R = [1] * n, [1] * n
        for i in range(1, n):
            L[i] = L[i - 1] * a[i - 1]
        for j in reversed(range(n - 1)):
            R[j] = R[j + 1] * a[j + 1]
        for i in range(n):
            L[i] = L[i] * R[i]
        return L
