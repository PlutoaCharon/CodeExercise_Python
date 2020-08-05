# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0

            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            # 　ls表示偷左子树能带来的最大收益，ln表示不偷左子树能带来的最大收益，rs、rn同理
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))
