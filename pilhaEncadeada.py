class linkedArray:
    class empty(Exception):
        pass

    class node:
            __slots__ = "elem", "nxt"

            def __init__(self, elem, nxt):
                self.elem = elem
                self.nxt = nxt

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def top(self):
        if self.isEmpty():
            raise self.empty("Stack is empty")
        else:
            return self.head.elem

    def push(self, elem):
        self.head = self.node(elem, self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise self.empty("Stack is empty")
        answer = self.head.elem
        self.head = self.head.nxt
        self.size += 1
        return answer