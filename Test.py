class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(0)  # 头结点，无存储，指向链表第一个结点
node = ListNode(1)
print(head.val, node.val, head.next)