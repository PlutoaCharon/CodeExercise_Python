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