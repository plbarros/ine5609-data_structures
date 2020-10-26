
class linkedList:
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

    def is_empty(self):
        return self.size == 0

    def get(self, elem):
        p = self.head
        while p != None and elem != p.elem:
            p = p.nxt
        return p

    def insert(self, elem, pos):
        p = self.node(elem, None)
        if pos==0:
            p.nxt = self.head
            self.head = p
        else:
            q = self.head
            i = 1
            while i < pos:
                q = q.nxt
                i += 1
            p.nxt = q.nxt
            q.nxt = p
        self.size += 1

    def remove(self, pos):
        if pos==0:
            value = self.head.elem
            self.head = self.head.nxt
        else:
            q = self.head
            i = 1
            while i < pos:
                q = q.nxt
                i += 1
            value = q.nxt.elem
            q.nxt = q.nxt.nxt
        self.size -= 1
        return value

