# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node):
        if not node: return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inorder(root)

        def dfs(start, end):
            if start == end: return TreeNode(nums[start])
            if start > end: return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)
            return root

        return dfs(0, len(nums) - 1)
