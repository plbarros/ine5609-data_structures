class circularList:
    class node:
            __slots__ = "elem", "nxt"

            def __init__(self, elem, nxt):
                self.elem = elem
                self.nxt = nxt

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def get(self, elem):
        if self.tail is None:
            return None
        else:
            pivot = self.tail.nxt
            while pivot != self.tail and pivot.elem != elem:
                pivot = pivot.nxt
            if pivot.elem != elem:
                return None
        return pivot

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        new = self.node(elem, None)
        if self.is_empty():
            self.tail = new
            self.tail.nxt = self.tail
        else:
            new.nxt = self.tail.nxt
            self.tail.nxt = new
        self.size += 1

    def remove(self, pivot):
        if self.tail == 1 or self.is_empty():
            self.tail = None
            self.size = 0
        else:
            pivot.nxt = pivot.nxt.nxt
            self.size -= 1