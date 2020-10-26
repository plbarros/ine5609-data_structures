class linkedList:
    class node:
            __slots__ = "elem", "nxt", "bck"

            def __init__(self, elem, nxt, bck):
                self.elem = elem
                self.nxt = nxt
                self.bck = bck

    def __init__(self):
        self.head = self.node(None,None,None)
        self.tail = self.node(None,None,None)
        self.head.nxt = self.tail
        self.tail.bck = self.head
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

    def insert_between(self, elem, suc, prev):
        p = self.node(elem, suc, prev)
        prev.nxt = p
        suc.bck = p
        self.size += 1

    def delete(self, node):
        prev = node.bck
        suc = node.nxt
        prev.nxt = suc
        suc.bck = prev
        e = node.elem
        node.bck = node.nxt = node.elem = None
        return e