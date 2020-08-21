# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            minDep = min(left, right) if left and right else left or right
            return 1 + minDep
