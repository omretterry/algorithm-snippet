# 索引优先队列
# 优先队列存在一个问题：无法在优先队列中，访问进入优先队列之前的原始数据
# 同样的，如果原始数据修改了，无法在优先队列中定位到那一个元素
# 为了解决以上问题，使用索引优先队列
class IndexMinPQ():
    # l 为优先队列的最大容量
    def __init__(self, l):
        self.n = 0  # 当前的最子节点索引
        self.pq = [-1 for _ in range(l + 1)]  # 用数组表示二叉堆，二叉堆为完全二叉树 存放索引
        # 存放对应索引的元素在优先队列中的索引,便于element元素找到对应的pq内的索引
        self.qp = [-1 for _ in range(l + 1)]
        self.elements = [None for _ in range(l + 1)]

    # 判断i索引和j索引对应元素的大小
    def less(self, i, j):
        return self.elements[self.pq[i]] < self.elements[self.pq[j]]

    # 交换两个元素
    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    # 下沉元素
    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j + 1, j):
                j += 1
            if not self.less(j, k):
                break
            self.exch(j, k)
            k = j

    # 上浮元素
    def swim(self, k):
        while k > 1 and self.less(k, k//2):
            self.exch(k//2, k)
            k //= 2

    # 插入元素
    def insert(self, i, v):
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.elements[i] = v
        self.swim(self.n)

    # 改变元素，将索引为i的元素替换为item
    # 实际元素的索引
    def change(i, item):
        self.elements[i] = item
        index = self.qp[i]
        self.swim(index)
        self.sink(index)

    # 删除索引i位置关联的元素
    # 优先队列中的索引
    def delete(i):
        d = self.pq[i]
        self.qp[d] = None
        self.elements[d] = None
        self.exch(i, self.n)
        self.n -= 1
        self.swim(self.pq[i])
        self.sink(self.pq[i])

    # 删除最小元素
    def delMin(self):
        if len(self.pq) <= 1:
            return None
        m = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.pq.pop(-1)
        self.sink(1)
        return self.elements[m]


m = IndexMinPQ(4)
m.insert(1, 4)
m.insert(2, 2)
m.insert(3, 1)
m.insert(4, 5)
print(m.delMin())
print(m.delMin())
print(m.delMin())
print(m.delMin())
