class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            # 逆时针
            matrix = list(zip(*matrix))[::-1]
        return res
    # 顺时针 matrix = map(list, zip(*(matrix[::-1])))