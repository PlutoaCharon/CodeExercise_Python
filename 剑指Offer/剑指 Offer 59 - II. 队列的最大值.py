class MaxQueue:
    """2个数组"""

    def __init__(self):
        self.queue = []
        self.max_stack = []

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.pop(0)
        if ans == self.max_stack[0]:
            self.max_stack.pop(0)
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
