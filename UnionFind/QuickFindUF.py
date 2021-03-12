class QuickFindUF():
    def __init__(self, n):
        self.count = n  # 联通分量的数量
        self.id = [i for i in range(n)]

    # 返回元素的联通分量的id
    def find(self, p):
        return self.id[p]

    # 合并两个节点
    def union(self, p, q):
      for i in self.id:
        if i == p:
          i = q
      self.count -= 1

        # 联通分量个数
    def counter(self):
        return self.n
