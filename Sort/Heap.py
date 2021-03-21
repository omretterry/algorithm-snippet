# 堆排序
# 实现复杂度O(nlogn)
class Heap():
    def __init__(self, l):
        self.l = l

    def exch(self, i, j):
        self.l[i], self.l[j] = self.l[j], self.l[i]

    def sink(self, i, n):
        while 2 * i + 1 <= n:
            j = 2 * i + 1
            if j < n and self.l[j] > self.l[j+1]:
                j += 1
            if self.l[j] >= self.l[i]:
                break
            self.exch(i, j)
            i = j

    def sort(self):
        n = len(self.l) - 1
        # 自底向上构造堆，否则可能出现顺序错误，父级不往下sink
        # e.g, [2,1,3,3,5,4,9]
        for i in range(n // 2, -1, -1):
            self.sink(i, n)
        while n > 0:
            self.exch(0, n)
            n -= 1
            self.sink(0, n)
        self.l.reverse()


l = [2, 3, 4, 1, 5, 3, 9]
h = Heap(l)
h.sort()
print(l)
