# 红黑树
# 优点：最优的查找插入效率
# 链接需要额外的空间（同BST）
# 首先需要理解2-3树的节点拓展策略

# 红黑树的5个性质
# 1.每个结点要么是红的要么是黑的
# 2.根结点是黑的
# 3.每个叶结点（叶结点即指树尾端NIL指针或NULL结点）都是黑的
# 4.如果一个结点是红的，那么它的两个儿子都是黑的（不存在两个连续的红色节点）
# 5.对于任意结点而言，其到叶结点树尾端NIL指针的每条路径都包含相同数目的黑结点 （也就是黑节点平衡）

# 算法4 中的红黑树实现： 基于 2-3树的 左倾红黑树 红节点只允许在左子节点

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from helper.TreeNode import RBTreeNode
from helper.TreeLog import print_rbtree


class RedBlackBst():
    def __init__(self):
        self.root = None

    def size(self, node):
        if node is None:
            return 0
        return node.size

    # 指向当前节点的链接是否为红链接
    def isRed(self, node):
        if node is None:
            return False
        return node.color is RBTreeNode.RED

    # 红链接右旋转
    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color, h.color = h.color, x.color
        h.size, x.size = x.size, h.size
        return x

    # 红链接左旋转
    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color, h.color = h.color, x.color
        h.size, x.size = x.size, h.size
        return x

    # 反转节点颜色
    def flipColor(self, node):
        node.left.color = RBTreeNode.BLACK if node.left.color is RBTreeNode.RED else RBTreeNode.RED
        node.right.color = RBTreeNode.BLACK if node.right.color is RBTreeNode.RED else RBTreeNode.RED
        node.color = RBTreeNode.BLACK if node.color is RBTreeNode.RED else RBTreeNode.RED
        return node

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = RBTreeNode.BLACK

    def _put(self, node, key, value):
        if node is None:
            return RBTreeNode(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.val = val

        # 情况1 插入在黑色节点下方
        # 情况1-1: 左子节点 不需要调整
        # 情况1-2: 右子节点 左旋 -> 情况 1-1
        # 情况1-2 比较难以理解的点是：会不会出现新插入的红色节点有一个黑色的兄弟节点，如果有，则左旋之后会破坏红黑树的黑色节点平衡的特性。
        # 为了证明不会有这种情况，需要从2-3树思考，如果新插入的红色节点有一个黑色的兄弟节点，说明插入的红色节点不是在2-3树的叶子节点，不满足插入特性

        # 情况2 插入在红色节点下方
        # 情况2-1: 左子节点 右旋（父节点） + 反色
        # 情况2-2: 右子节点 左旋 -> 情况 2-1

        # 综上，红黑树插入主要考虑红色节点处插入的向上生长的过程
        # 总结情况1 和 情况2 可以得出算法4中的简化的代码

        print_rbtree(node)

        # 红黑树节点操作

        # 如果将nil节点考虑进去，情况2-2前半部分的操作就可以和情况1-2合并 即 不管新插入的节点是插入在红色节点还是黑色节点下方，
        # 右节点是红色的，且不是需要反色的情况（左节点不是红的），就先左旋
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
            print("rotate left:")
            print_rbtree(node)

        # 这个地方一个理解的难点是，左旋和右旋操作不会在一次递归里面同时执行的，因为情况2-1右旋的对象是父节点
        # 所以下面两个操作放在 else 条件里也不会有问题， 算法4中，没有放在else里，Robert大佬只是将他们统一了状态转移，简化了条件
        else:
            if self.isRed(node.left) and self.isRed(node.left.left):
                node = self.rotateRight(node)
                print("rotate right:")
                print_rbtree(node)
            if self.isRed(node.left) and self.isRed(node.right):
                node = self.flipColor(node)
                print("flip color:")
                print_rbtree(node)

        node.size = self.size(node.left) + self.size(node.right) + 1
        return node



# 操作部分
rbbst = RedBlackBst()
testData = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]
for item in testData:
    print('put:', item[0], ":", item[1])
    rbbst.put(item[0], item[1])
    print_rbtree(rbbst.root)

print_rbtree(rbbst.root)
