class WeightedQuickUnoinUF():
  def __init__(self,n):
    self.count = n
    self.id = [i for i in range(n)]
    self.sz = [1 for i in range(n)]

  def find(self, p):
    orgP = p

    while self.id[p] != p:
      p = self.id[p]

    # 路径压缩的带权quick union
    # 路径压缩
    while self.id[orgP] != orgP:
      orgP = self.id[orgP]
      self.id[orgP] = p

    return p
  
  def union(self, p, q):
    rootP = self.find(p)
    rootQ = self.find(q)
    if rootP == rootQ:
      return
    if self.sz[rootP] > self.sz[rootQ]:
      self.id[rootQ] = rootP
      self.sz[rootP] += self.sz[rootQ]
    else:
      self.id[rootP] = rootQ
      self.sz[rootQ] += self.sz[rootP]
    self.count -= 1

  def counter(self):
    return self.count