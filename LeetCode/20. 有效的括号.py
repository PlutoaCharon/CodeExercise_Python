class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in {'(', '{', '['}:
                stack.append(i)
            elif len(stack) == 0:
                # 多了右括号
                return False
            elif dic[stack[-1]] == i:
                stack.pop()
            else:
                # 括号i处不匹配
                return False
        return True if not stack else False

if __name__ == '__main__':
    s = Solution()
    ans = s.isValid("(])")
    print(ans)