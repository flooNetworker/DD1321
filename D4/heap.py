
class HeapNode:

    def __init__(self, data, priority):
        """data är det objekt vi vill lagra
           priority är nyckelvärdet som används för att jämföra objekten"""
        self.data = data
        self.priority = priority


class Heap:
    # En max-heap

    def __init__(self, maxsize):
        """Skapar en lista där vi använder element 1..maxsize"""
        self.maxsize = maxsize
        self.tab = (maxsize+1)*[None]
        self.size = 0

    def isEmpty(self):
        """Returnerar True om heapen är tom, False annars"""
        return self.size == 0

    def isFull(self):
        """Returnerar True om heapen är full, False annars"""
        return self.size == self.maxsize

    def put(self, data, priority):
        """Lägger in nya data med nyckeln priority i heapen"""
        if not self.isFull():
            self.size += 1
            self.tab[self.size] = HeapNode(data, priority)
            i = self.size
            while i > 1 and self.tab[i//2].priority < self.tab[i].priority:
                self.tab[i//2], self.tab[i] = self.tab[i], self.tab[i//2]
                i = i//2

    def get(self):
        """Hämtar det största (översta) objektet ur heapen"""
        if not self.isEmpty():
            data = self.tab[1]
            self.tab[1] = self.tab[self.size]
            self.size -= 1
            i = 1
            while i <= self.size//2:
                maxi = self.maxindex(i)
                if self.tab[i].priority < self.tab[maxi].priority:
                    self.tab[i], self.tab[maxi] = self.tab[maxi], self.tab[i]
                i = maxi
            return data.data
        else:
            return None

    def maxindex(self, i):
        """Returnerar index för det största barnet"""
        if 2*i+1 > self.size:
            return 2*i
        if self.tab[2*i].priority > self.tab[2*i+1].priority:
            return 2*i
        else:
            return 2*i+1
