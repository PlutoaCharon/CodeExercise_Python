#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 找到只出现一次的数字
# @param array int整型一维数组
# @return int整型
#
class Solution:
    def findNum(self , array ):
        # write code here
        if not array:
            return 0
        tmp = array[0]
        for i in range(1, len(array)):
            tmp = tmp ^ array[i]
        return tmp