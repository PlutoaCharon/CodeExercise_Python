class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 将字符串反转
        a = num1[::-1]
        b = num2[::-1]
        res = 0
        # 循环num2
        # 假如num1 = 123 num2 = 456
        # 则从6 * 3 * 0 + 6 * 2 * 10 + 6 * 1 * 100开始
        for i, x in enumerate(b):
            temp_res = 0
            for j, y in enumerate(a):
                temp_res += int(x) * int(y) * 10 ** j
            res += temp_res * 10 ** i

        return str(res)


if __name__ == '__main__':
    s = Solution()
    ans = s.multiply("123", "456")
    print(ans)
