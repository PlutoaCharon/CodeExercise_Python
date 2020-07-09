dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"

dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵
for i in range(len(sentence)):
    dp[i] = dp[i - 1] + 1
    # 遍历所有单词，看能否和「以i为结尾的子串」一样
    for dic in dictionary:
        if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
            dp[i] = min(dp[i], dp[i - len(dic)])
print(dp[-2])