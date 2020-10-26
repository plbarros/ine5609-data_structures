class list:
    class element:
        def __init__(self, value, nxt):
            self.value = value
            self.nxt = nxt

    def __init__(self, capacity):
        self.list = [None]*capacity
        self.n = 0

    def get(self, pos):
        return self.list[pos]

    def isEmpty(self):
        return self.n == 0

    def add(self, value):
        e = self.element(value, None)
        if self.isEmpty():
            self.list[0] = e
            e.nxt = 1
            self.n += 1
        elif self.n == len(self.list) - 1:
            return print("Full list!")
        else:
            self.list[self.n] = e
            e.nxt = self.n + 1
            self.n += 1

    def remove(self, pos):
        if self.isEmpty():
            return print("Empty list!")
        else:
            q = self.list[0]
            while q < self.n and q.nxt != self.list[pos]:
                q = q.nxt
            if q == self.list[pos] and q.nxt != len(self.list + 1):
                q.nxt = q.nxt.nxt
                self.n -= 1


