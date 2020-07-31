# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归做法：
        if len(preorder) == 0:
            return None

        ind = inorder.index(preorder[0])  # 根节点
        root = TreeNode(preorder[0])

        left = self.buildTree(preorder[1:ind + 1], inorder[:ind])
        right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])

        root.left = left
        root.right = right

        return root