class Solution:
    def reverse(self, x: int) -> int:
        # 将整数的绝对值转换成字符串
        s = str(abs(x))
        # 翻转字符串
        s = s[::-1]
        # 如果输入整数是负数，增加负号
        if x < 0:
            s = '-' + s
        # 转换为整数
        result = int(s)
        # 判断是否溢出
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0
