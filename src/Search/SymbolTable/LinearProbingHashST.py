# 线性探测的散列表
# 插入时：hash 碰撞之后，将值放在后续中的第一个值为空的元素中
# 查找是：找到对应的hash值，发现键值不一致，向后探索，直到找到对应的键，如果为空，说明查找结束

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))


class LinearProbingHashST():
    # M 为存放散列值的数组长度
    # 线性探测的散列表的数组长度需要大于键值对的个数
    def __init__(self, M):
        self.M = M
        self.keys = [None for _ in range(M)]
        self.vals = [None for _ in range(M)]

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] != key and self.keys[i] != None:
            i = (i + 1) % self.M
        return self.vals[i]

    def put(self, key, val):
        i = self.hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            # 查到数组最后一个还是没有空位，再从头开始查找
            i = (i + 1) % self.M
        self.keys[i] = key
        self.vals[i] = val

    # 删除操作
    # 不能直接设置为None，这样后续的键值就无法查找
    def delete(self, key):
        if key not in self.keys:
          return
        i = self.hash(key)
        # 一定能在None结束符之前找到对应的key（找不到的情况已经return）
        while self.keys[i] != key:
          i = (i + 1) % self.M
        self.keys[i] = None
        self.vals[i] = None
        i = (i + 1) % self.M
        # 删除之后将每一个都往前挪
        while self.keys[i] != None:
          k = self.keys[i]
          v = self.vals[i]
          self.keys[i] = None
          self.vals[i] = None
          self.put(k, v)
          i = (i + 1) % self.M


# test
t = "searchexample"
st = LinearProbingHashST(len(t))
for i in range(len(t)):
    print('put', t[i], i)
    st.put(t[i], i)

for k in t:
    print('get:', '[' + k + ']', st.get(k))

print('keys: ', st.keys)
print('vals: ', st.vals)
st.delete('e')
print(st.get('e'))
