'''
近似周期串
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小明发现有的字符串中蕴含着一些规律，但是它们又和普通的周期串有点不一样。例如：ABCABDABDABE。如果以3为周期，可以看到其中包含“ABC”、“ABD”和“ABE”等子串，其中“ABD”出现了两次。

这些子串两两之间最多只有某一位上的字符不相同，其他位置上的字符都一样。小明将其称为“近似串”，由多个“近似串”组成的字符串称为“近似周期串”。“近似周期串”中的每一个“近似串”的长度需大于等于2。

需要注意的是“ABCABBACD”并不是一个“近似周期串”。如果以3为周期，其子串包括“ABC”、“ABB”和“ACD”，“ABB”与“ACD”、“ABC”与“ACD”均存在两个位置上的字符不相同，因此不是“近似周期串”。特别的，“AAAAAA”也是一个“近似周期串”，因为它满足上述“近似周期串”的定义。

现在给你一个字符串，请编写一个程序判断该字符串是否是以3为周期的“近似周期串”。



输入描述
多组输入，第1行输入一个正整数T表示输入数据的组数。

对于每一组输入数据：输入一个长度不超过1000的字符串，字符串中只包含大写英文字母。

输出描述
针对每一组输入数据，输出该字符串是否是以3为周期的“近似周期串”，如果是输出“Yes”，否则输出“No”。


样例输入
2
ABCABDABDABEABEABF
ABCABDAEC
样例输出
Yes
No
'''
while True:
    n = int(input())
    for _ in range(n):
        s = input()
        if not s or len(s) <= 2:
            print("No")
        arr, ans = [], []  # ['ABC', 'ABD', 'AEC']
        # 存储到arr中
        for i in range(0, len(s), 3):
            arr.append(s[i:i + 3])
        length = len(arr)
        for i in range(length - 1):
            for j in range(i + 1, length):
                tmp = 0
                for k in range(3):
                    if arr[i][k] == arr[j][k]:
                        # print(arr[i][k], arr[j][k])
                        continue
                    else:
                        # print(arr[i][k], arr[j][k])
                        tmp += 1
                if tmp == 2:
                    ans.append("No")
                    break
        if not ans:
            print("Yes")
        else:
            print("No")
