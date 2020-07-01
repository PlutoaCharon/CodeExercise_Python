'''
elephant elephant
elephant tiger
elephant cat
elephant mouse

tiger elephant
tiger tiger
tiger cat
tiger mouse

cat elephant
cat tiger
cat cat
cat mouse

mouse elephant
mouse tiger
mouse cat
mouse mouse
'''
str1, str2 = map(str, input().split())
arr1 = ["elephant","tiger","cat"]

if str1 not in arr1:
    # str1 = mouse
    if str2 not in arr1:
        print("tiangou yiwusuoyou")
    else:
        if len(str2) == 8:
            print("tiangou yiwusuoyou")
        else:
            print("tiangou txdy")
else:
    if str2 in arr1:
        if len(str1) >= len(str2):
            print("tiangou yiwusuoyou")
        else:
            print("tiangou txdy")
    else:
        if len(str1) == 8:
            print("tiangou txdy")
        else:
            print("tiangou yiwusuoyou")