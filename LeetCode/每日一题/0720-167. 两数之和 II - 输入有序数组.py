class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 1, len(numbers)
        while index1 < index2:
            tmp = numbers[index1 - 1] + numbers[index2 - 1]
            if tmp == target:
                return [index1, index2]
            elif tmp < target:
                index1 += 1
            else:
                index2 -= 1
        return [-1, -1]