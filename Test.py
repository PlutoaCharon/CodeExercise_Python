# # # # import collections
# # # # from collections import defaultdict
# # # # nums1 = [4,9,5]
# # # # nums2 = [9,4,9,8,4]
# # # #
# # # # dct1 = defaultdict(int)
# # # # for i in nums1:
# # # #     dct1[i] += 1
# # # # dct2 = defaultdict(int)
# # # # for i in nums2:
# # # #     dct2[i] += 1
# # # #
# # # # # print(dct1)
# # # # # print(dct2)
# # # # # print(set(dct1))
# # # # # print(set(dct2))
# # # # # print(set(dct1)&set(dct2))
# # # #
# # # #
# # # # m = collections.Counter()
# # # # for num in nums1:
# # # #     m[num] += 1
# # # # print(m)
# # # # print(set(m))
# # # # print(sorted(m.elements()))
# # # # print(m.items())
# # # import time
# # #
# # # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # res = []
# # # # while matrix:
# # # #     res.append(matrix.pop(0))
# # # #     matrix = list(zip(*matrix))[::-1]
# # # #     print(matrix)
# # # #     print(res)
# # # while matrix:
# # #     matrix = list(zip(*matrix))
# # #     matrix.pop(0)
# # #     matrix1 = matrix[::-1]
# # #
# # #     print("matrix = ", matrix)
# # #     print("matrix1 = ", matrix1)
# # #
# # #
# # #     time.sleep(1)
# # #
# # #
# # left = [1, 2, 3]
# # right = [4, 5, 6]
# # res = []
# # for l in left:
# #     for r in right:
# #         tmp = [l, r]
# #         res.append(tmp)
# # print(res)
# tmp = ["flower", "flow", "flight"]
# res = tmp[0]
#
# i = 1
# while i < len(tmp):
#     print(tmp[i].find(res))
#     while tmp[i].find(res) != 0:
#         res = res[0: len(res) - 1]
#     i = i + 1
# print(res)

# print(1e9 + 7)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix = list(map(list, zip(*(matrix[::-1]))) 顺时针
# # matrix = list(map(list, zip(*matrix)))[::-1]  逆时针
# print(matrix)
s = "123456789"
print(s.index("12"))