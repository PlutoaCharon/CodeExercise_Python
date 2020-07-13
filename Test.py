import collections
from collections import defaultdict
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

dct1 = defaultdict(int)
for i in nums1:
    dct1[i] += 1
dct2 = defaultdict(int)
for i in nums2:
    dct2[i] += 1

# print(dct1)
# print(dct2)
# print(set(dct1))
# print(set(dct2))
# print(set(dct1)&set(dct2))


m = collections.Counter()
for num in nums1:
    m[num] += 1
print(m)
print(set(m))
print(sorted(m.elements()))
print(m.items())