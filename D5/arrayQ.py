class ArrayQ:
    def __init__(self):
        self.items = []  # queue is empty at first
        self.size = 0

    def isEmpty(self):
        return self.items == []  # check if queue is empty, return True if empty

    def enqueue(self, item):
        self.size += 1
        self.items.append(item)  # enqueue items on index 0

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)  # return items last in line (default is -1)

    def size_of(self):
        return self.size-1
