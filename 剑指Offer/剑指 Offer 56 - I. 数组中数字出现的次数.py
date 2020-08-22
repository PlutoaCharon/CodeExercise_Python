class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here

        # 将组内元素异或，返回异或后的结果
        def XORarray(array):
            result = 0
            for i in range(len(array)):
                result ^= array[i]
            return result

        # 从低到高找到第一位为1的数
        # 与1(01)按位与&，0&1=0 0&0=0 1&0=0 1&1=1
        # 如果结果是0,则与2(10)按位与,直到找到让结果是1的theNum
        def getFirstBitIs1(num):
            theNum = 0
            while num & theNum == 0:
                theNum += 1
            return theNum

        num = XORarray(array)
        firstBitNum = getFirstBitIs1(num)
        result = [0, 0]
        # 分组进行异或
        for i in range(len(array)):
            if array[i] & firstBitNum == 0:
                result[0] ^= array[i]
            else:
                result[1] ^= array[i]
        return result
