n, m = 2, 5  # 2的5次方
sum = 1
tmp = n

while m != 0:
    if m & 1 == 1:
        sum *= tmp
    tmp *= tmp
    m = m >> 1

print(sum)
