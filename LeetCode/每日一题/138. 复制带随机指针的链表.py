"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head:
                return None
            if head in vis:
                return vis[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            vis[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        vis = {}
        return dfs(head)