def findNumber(num):
    if not 1 <= num <= 2147483647:
        return [-1, -1]
    if num == 1:
        return [2, -1]
    if num == 2147483647:
        return [-1, -1]
    if num == 2147483646:
        return [-1, 1073741823]

    num1 = format(num, 'b').count("1")
    maxans = num + 1
    minans = num - 1
    while bin(maxans).count("1") != num1:
        if maxans < 2147483647:
            maxans += 1
        else:
            maxans = -1
            break
    while bin(minans).count("1") != num1:
        if minans > 1:
            minans -= 1
        else:
            minans = -1
            break
    return [maxans, minans]
