# 　使用duque
'''
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
'''

# 使用列表
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            out = []
            for i in queue:
                res.append(i.val)
                if i.left:
                    out.append(i.left)
                if i.right:
                    out.append(i.right)
            queue = out
        return res