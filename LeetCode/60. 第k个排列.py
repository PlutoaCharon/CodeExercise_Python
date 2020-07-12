# 第一种 全排列返回
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = list(permutations([str(i) for i in range(1, n + 1)], n))
        return "".join(arr[k - 1])

# 第二种 逆康托展开
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * (n + 1)  # 多一个 0 的阶乘
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        k = k - 1 # 康拓展开的X值
        nums = [_ for _ in range(1, n + 1)] # 递增数组
        ans = [] # 答案
        for i in range(1, n + 1):
            index, k = divmod(k, fact[n - i]) # index 要取出数的下标
            ans.append(nums.pop(index))
        return "".join(map(str, ans))