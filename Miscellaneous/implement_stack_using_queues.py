class MyStack:

    def __init__(self):
        self.main_queue = []
        self.secondary_queue = []

    def push(self, x: int) -> None:
        self.main_queue.insert(0, x)

    def pop(self) -> int:
        while len(self.main_queue) > 1:
            elem = self.main_queue.pop()
            self.secondary_queue.insert(0, elem)
        ret = self.main_queue.pop()
        self.main_queue = self.secondary_queue
        self.secondary_queue = []
        print(f"{self.main_queue=}, {self.secondary_queue=}")
        return ret

    def top(self) -> int:
        while len(self.main_queue) > 1:
            elem = self.main_queue.pop()
            self.secondary_queue.insert(0, elem)
        ret = self.main_queue[0]
        self.main_queue.extend(self.secondary_queue)
        self.secondary_queue = []
        print(f"{self.main_queue=}, {self.secondary_queue=}")
        return ret

    def empty(self) -> bool:
        return len(self.main_queue) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())
print(obj.empty())
