import bisect

nums = [5, 2, 5, 6, 1]

sorted_nums = []
ans = []
for n in nums[::-1]:
    index = bisect.bisect_left(sorted_nums, n)
    bisect.insort(sorted_nums, n)
    ans.append(index)
print(ans[::-1])
