class Solution:
    def isValid(self, s: str) -> bool:
        stack, dic = [], {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in {'(', '{', '['}:
                stack.append(i)
            elif not stack:
                return False
            elif dic[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return True if not stack else False
