# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 右根左 非递归遍历
        stack, p, count = [], root, 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            curr = stack.pop()
            count += 1
            if count == k: return curr.val
            p = curr.left
