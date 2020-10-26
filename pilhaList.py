class arrayStack:
    class empty(Exception):
        pass

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def top(self):
        if self.isEmpty():
            raise self.empty("Stack is empty")
        else:
            return self.data[-1]

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if self.isEmpty():
            raise self.empty("Stack is empty")
        else:
            self.data.pop()

    

