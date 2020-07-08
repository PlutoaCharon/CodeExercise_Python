class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = shorter * (k - i) + longer * i
        return res