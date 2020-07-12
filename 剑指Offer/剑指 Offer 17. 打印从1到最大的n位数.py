class Solution:
    def printNumbers(self, n: int) -> List[int]:
        num = 1
        ans = []
        while len(str(num)) <= n:
            ans.append(num)
            num += 1
        return ans

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n <= 0:
            return []
        return list(range(1, 10 ** n))