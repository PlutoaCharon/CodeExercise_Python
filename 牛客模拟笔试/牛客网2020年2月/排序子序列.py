n = input()
a = list(map(int, input().split()))

if n == 1 or n == 2:
    print(1)

ans = 1
flag = 0  # 1增 0平 -1减
for i in range(1, len(a)):

    if flag == 0:
        if a[i - 1] < a[i]:
            flag = 1
        elif a[i - 1] > a[i]:
            flag = -1
    elif (flag < 0) == (a[i] > a[i - 1]):

        ans += 1
        flag = 0

print(ans)
