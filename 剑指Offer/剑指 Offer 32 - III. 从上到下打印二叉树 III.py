# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            size = len(queue)
            out = []
            for i in range(size):
                r = queue.pop(0)
                out.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            if len(res) & 1:
                res.append(out[::-1])
            else:
                res.append(out)
        return res