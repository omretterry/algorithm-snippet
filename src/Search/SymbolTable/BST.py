# 二叉搜索树
# 实现简单，能够实现有序性的相关操作
# 可能退化成链表导致时间复杂度增加

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from helper.TreeNode import TreeNode


class BST():
    def __init__(self):
        self.root = None

    # 节点数量
    def size(self, node):
        if node is None:
            return 0
        else:
            return node.size

    # 获取key内容
    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    # 插入信息
    def put(self, key, val):
        if self.root is None:
            self.root = TreeNode(key=key, val=val)
        else:
            self._put(self.root, key, val)

    def _put(self, node, key, val):
        if node is None:
            return TreeNode(key=key, val=val)
        if key > node.key:
            node.right = self._put(node.right, key, val)
        elif key < node.key:
            node.left = self._put(node.left, key, val)
        else:
            node.val = val
        node.size = self.size(node.left) + self.size(node.right) + 1
        return node

    # 最小值
    def min(self):
        return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    # 向下取整
    def floor(self, key):
        return self._floor(self.root, key)

    def _floor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if node.key > key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        if t is None:
            return node
        else:
            return t

    # 找出排名为K的元素
    def select(self, k):
        return self._select(self.root, k)

    def _select(self, node, k):
        if node is None:
            return None
        t = self.size(node.left)
        if k < t:
            return self._select(node.left, k)
        elif k > t:
            return self._select(node.right, k - t - 1)
        else:
            return node

    # 排名 表示小于制定key有多少个元素
    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return self.size(node.left) + self._rank(node.right, key) + 1
        else:
            return self.size(node.left)

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.size = self.size(node.left) + self.size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            t = node
            if t.right is None:
                return t.left
            if t.left is None:
                return t.right
            # node 的后继节点
            node = self._min(t.right)
            self._deleteMin(t.right)
        node.size = self.size(node.left) + self.size(node.right) + 1
        return node

    # 获取指定范围中的key
    def keys(self, lo, hi):
        keys = []
        self._keys(self.root, lo, hi, keys)
        return keys

    def _keys(self, node, lo, hi, keys):
        if node is None:
            return None
        if node.key < hi:
            self._keys(node.left, lo, hi, keys)
        if node.key <= hi and node.key >= lo:
            keys.append(node.key)
        if node.key > lo:
            self._keys(node.right, lo, hi, keys)


bst = BST()
testData = [
    (4, 'F'),
    (2, 'E'),
    (5, 'A'),
    (1, 'B'),
    (6, 'C'),
]
for item in testData:
    print('put:', item[0], ":", item[1])
    bst.put(item[0], item[1])

for item in testData:
    print('get [' + str(item[0]) + ']:', bst.get(item[0]))

print('min:', bst.min().val)
print('floor:', bst.floor(7).val)
print('select:', bst.select(3).val)
print('rank:', bst.rank(3))
print('keys:', bst.keys(2, 5))
print('delete min > ')
bst.deleteMin()
print('min', bst.min().val)
print('delete > 2')
bst.delete(2)
print('min', bst.min().val)
print('delete > 4')
bst.delete(4)
print('min', bst.min().val)
