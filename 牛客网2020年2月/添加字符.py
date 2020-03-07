str1 = input()
str2 = input()
len_str1 = len(str1)
len_str2 = len(str2)
ans = len_str1

if len_str1 < len_str2:
    i = 0
    while i+len_str1 <= len_str2:
        cnt = 0
        for j in range(len_str1):
            if str1[j] != str2[i+j]:
                cnt +=1
        if cnt < ans:
            ans = cnt
        i += 1
else:
    cnt = 0
    for j in range(len_str1):
        if str1[j] != str2[j]:
            cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)