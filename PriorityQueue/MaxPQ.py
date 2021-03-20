# 基于堆的优先队列
# 插入元素和删除最大元素的时间复杂度都是O(logN)
class MaxPQ():
    def __init__(self):
        self.n = 0  # 当前的最子节点索引
        self.pq = [None]  # 用数组表示二叉堆，二叉堆为完全二叉树

    # 下沉元素
    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] >= self.pq[j]:
                break
            self.pq[j], self.pq[k] = self.pq[k], self.pq[j]
            k = j

    # 上浮元素
    def swim(self, k):
        while k > 1 and self.pq[k//2] < self.pq[k]:
            self.pq[k//2], self.pq[k] = self.pq[k], self.pq[k//2]
            k //= 2

    # 插入元素
    def insert(self, v):
        self.n += 1
        self.pq.append(v)
        self.swim(self.n)

    # 删除最大元素
    def delMax(self):
        if len(self.pq) <= 1:
            return None
        m = self.pq[1]
        self.pq[1], self.pq[self.n] = self.pq[self.n], self.pq[1]
        self.n -= 1
        self.pq.pop(-1)
        self.sink(1)
        return m


m = MaxPQ()
m.insert(4)
m.insert(2)
m.insert(1)
m.insert(5)
print(m.delMax())
print(m.delMax())
print(m.delMax())
print(m.delMax())
