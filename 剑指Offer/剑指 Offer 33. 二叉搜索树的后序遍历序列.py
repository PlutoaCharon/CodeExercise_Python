class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float("inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
