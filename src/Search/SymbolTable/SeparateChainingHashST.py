# 拉链法的散列表
# 基于链表实现的符号表

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from SequentialSearchST import SequentialSearchST


class SeparateChaingHashST():
    # M 为存放散列值的数组长度
    def __init__(self, M):
        self.M = M
        self.st = [SequentialSearchST() for _ in range(M)]

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def get(self, key):
        return self.st[self.hash(key)].get(key)
    
    def put(self, key, val):
        self.st[self.hash(key)].put(key, val)

#test
st = SeparateChaingHashST(97)
t = "searchexample"
for i in range(len(t)):
    print('put', t[i] ,i)
    st.put(t[i], i)

for k in t:
    print('get:', '[' + k + ']', st.get(k))


