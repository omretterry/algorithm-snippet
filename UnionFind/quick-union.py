class QuickUnionUF():
    def __init__(self, n):
        self.count = n
        self.id = [i for i in range(n)]

    def find(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.id[rootP] = rootQ
        self.count -= 1

    def counter(self):
        return self.count
