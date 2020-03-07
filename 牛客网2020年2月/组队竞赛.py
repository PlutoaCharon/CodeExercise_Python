'''
输入:
2
5 2 8 5 1 5
输出:
10
'''
n = int(input())
list1 = list(map(int, input().split()))
list1 = sorted(list1, reverse=True)
ans = 0
for i in range(n):
    ans += int(list1[2*i+1])
print(ans)