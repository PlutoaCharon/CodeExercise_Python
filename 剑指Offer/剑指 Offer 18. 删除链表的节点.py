# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 如果头结点为空，直接返回
        if not head:
            return head
        # 如果头结点值等于val，直接返回head.next（题设中有注明链表中元素不重复）
        if  head.val == val:
            return head.next
        # 定义一个指针
        cur = head
        while cur.next:
            # 关键步骤，如果next的值等于val，跳过该节点
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
