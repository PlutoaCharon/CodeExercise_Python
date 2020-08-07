x, y = 1, 2
print("交换前：", x, y)

x = x ^ y
print(x, y)
y = x ^ y
print(x, y)
x = x ^ y
print(x, y)

print("交换后：", x, y)
