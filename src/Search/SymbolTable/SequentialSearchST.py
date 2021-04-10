# 顺序查找的符号表
# 基于链表
# 优点：适用于小型应用
# 缺点：对于大型符号表很慢

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from helper.Node import Node


class SequentialSearchST():
    def __init__(self):
        self.st = Node()

    def get(self, key):
        node = self.st
        while node != None:
            if (node.key == key):
                return node.val
            node = node.next
        return None

    def put(self, key, val):
        node = self.st
        while node != None:
            if (node.key == key):
                node.val = val
                return
            node = node.next
        self.st = Node(key, val, self.st)


# test
t = "searchexample"
st = SequentialSearchST()
for i in range(len(t)):
    st.put(t[i], i)

for k in t:
    print(st.get(k))
