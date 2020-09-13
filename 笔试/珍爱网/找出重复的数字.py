#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 输出结果重复的数字
# @param arrs int整型一维数组
# @return int整型
#
class Solution:
    def getResult(self, arrs):
        # write code here
        for i in range(32):
            while i != arrs[i]:
                if arrs[i] == arrs[arrs[i]]:
                    return arrs[i]
                tmp = arrs[i]
                arrs[i], arrs[tmp] = arrs[tmp], arrs[i]

        '''
        dic = {}
        for i in arrs:
            if i not in dic:
                dic[i] = 1
            else:
                return i
        '''