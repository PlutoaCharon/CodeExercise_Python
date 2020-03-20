'''
链接：https://www.nowcoder.com/questionTerminal/bfb60fce32974c45a806e567e17183ba
来源：牛客网

牛牛有n张卡片排成一个序列.每张卡片一面是黑色的,另一面是白色的。初始状态的时候有些卡片是黑色朝上,有些卡片是白色朝上。牛牛现在想要把一些卡片翻过来,得到一种交替排列的形式,即每对相邻卡片的颜色都是不一样的。牛牛想知道最少需要翻转多少张卡片可以变成交替排列的形式。

输入描述:
输入包括一个字符串S,字符串长度length(3 ≤ length ≤ 50),其中只包含'W'和'B'两种字符串,分别表示白色和黑色。整个字符串表示卡片序列的初始状态。


输出描述:
输出一个整数,表示牛牛最多需要翻转的次数。
示例1
输入
BBBW
输出
1
'''
ans1 = 0
ans2 = 0
strq1 = list(input())
strq2 = strq1[::-1]

for i in range(len(strq1) - 1):
    if strq1[i] == strq1[i + 1]:
        ans1 += 1
        if strq1[i] == "B":
            strq1[i + 1] = "W"
        else:
            strq1[i + 1] = "B"
    else:
        continue

for i in range(len(strq2) - 1):
    if strq2[i] == strq2[i + 1]:
        ans2 += 1
        if strq2[i] == "B":
            strq2[i + 1] = "W"
        else:
            strq2[i + 1] = "B"
    else:
        continue

print(min(ans1, ans2))