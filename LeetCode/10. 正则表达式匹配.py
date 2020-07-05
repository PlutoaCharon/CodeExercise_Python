s = "aab"
p = "c*a*b"
ns = len(s)
np = len(p)

dp = [[False] * (np + 1) for _ in range(ns + 1)]
dp[0][0] = True
# 匹配空字符串的情况, 匹配串为空时已经为False, 不再更新
for i in range(np):
    # 根据规则, *前必存在一个字符, 则当前为*时, 其状态与前2的状态一致
    if p[i] == '*' and dp[0][i - 1]:
        dp[0][i + 1] = True
# 更新状态矩阵
for i in range(1, ns + 1):
    for j in range(1, np + 1):
        # i,j是矩阵的行与列, 对应到匹配串和字符串的索引要-1
        # 匹配串与字符串匹配(相等或为.)传递状态
        if p[j - 1] == s[i - 1] or p[j - 1] == '.':
            dp[i][j] = dp[i - 1][j - 1]
        # 匹配串中 * 字符特殊处理
        elif p[j - 1] == '*':
            # 根据匹配规则, 比较匹配串*的前一个字符与字符串中前一个字符
            # 二者不相等时, a*只有作为空字符串时才可能匹配,
            # 这就是说, 略过前一个字符, *字符对应的状态与字符串中前2个字符的状态一致
            if p[j - 2] != s[i - 1]:
                dp[i][j] = dp[i][j - 2]
            # 二者相等时有三种情况
            # a*作为: 空字符, 单字符 a, 多字符 aaa...
            if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
print(dp[-1][-1])
