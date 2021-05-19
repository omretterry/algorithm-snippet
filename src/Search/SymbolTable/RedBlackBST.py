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

# 算法4 中的红黑树实现： 基于 2-3树的 左倾红黑树（LLRB - left-leaning rb tree） 红节点只允许在左子节点

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
        return self.root

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

        # print_rbtree(node)

        # 红黑树节点操作

        # 如果将nil节点考虑进去，情况2-2前半部分的操作就可以和情况1-2合并 即 不管新插入的节点是插入在红色节点还是黑色节点下方，
        # 右节点是红色的，且不是需要反色的情况（左节点不是红的），就先左旋
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
            # print("rotate left:")
            # print_rbtree(node)

        # 这个地方一个理解的难点是，左旋和右旋操作不会在一次递归里面同时执行的，因为情况2-1右旋的对象是父节点
        # 所以下面两个操作放在 else 条件里也不会有问题， 算法4中，没有放在else里，Robert大佬只是将他们统一了状态转移，简化了条件
        else:
            if self.isRed(node.left) and self.isRed(node.left.left):
                node = self.rotateRight(node)
                # print("rotate right:")
                # print_rbtree(node)
            if self.isRed(node.left) and self.isRed(node.right):
                node = self.flipColor(node)
                # print("flip color:")
                # print_rbtree(node)

        node.size = self.size(node.left) + self.size(node.right) + 1
        return node

    # 删除节点部分 ----- start -----

    # 删除节点调整节点不为2-节点的方法
    # 从右节点借节点过来
    def _moveRedLeft(self, node):
        # 情况0: 当前节点不是一个2-节点，不用操作
        # 情况1: 当前节点是一个2-节点，兄弟节点借不出来（也是一个2-节点） 合并成一个临时的4-节点
        # 情况2: 当前节点是一个2-节点，兄弟节点能够借出来，借一个过来变成一个3-节点

        # 这是正常思路，但是算法4中的节点是没有定义指向父亲节点的指针的，所以递归中无法简单的拿到当前节点的兄弟节点
        # 所以这边在父节点的时候，帮助左子节点进行调整
        if not self.isRed(node.left) and not self.isRed(node.left.left):
            # 左右子节点都是2-节点
            if not self.isRed(node.right.left):
                node.color = RBTreeNode.BLACK
                node.left.color = RBTreeNode.RED
                node.right.color = RBTreeNode.RED
            else:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)
                node.right.color = RBTreeNode.BLACK
                node.left.left.color = RBTreeNode.RED

        return node

    # 从左节点借节点过来
    def _moveRedRight(self, node):
        # 右节点是黑色节点
        if not self.isRed(node.right) and not self.isRed(node.right.left):
            # 左右子节点都是2-节点
            if not self.isRed(node.left) and not self.isRed(node.left.left):
                node.color = RBTreeNode.BLACK
                node.left.color = RBTreeNode.RED
                node.right.color = RBTreeNode.RED
            else:
                node = self.rotateRight(node)
                node.color = RBTreeNode.BLACK
                node.right.color = RBTreeNode.RED
                # node.left.color = RBTreeNode.BLACK
                # node.right.color = RBTreeNode.RED
                # node.right = self.flipColor(node.right)
                # node.right = self.rotateLeft(node.right)
        return node

    # 删除操作结束后，向上平衡红黑树（分解临时的4-节点）
    def _blance(self, node):
        # delmin 平衡中只需左旋
        if self.isRed(node.right):
            # 节点左旋，我们是用的moveRedLeft方式，保证了只有带删除的叶子节点可能是一个临时的4-节点
            # 其他的父亲节点可能为右节点为红色的3-节点（如果是4-节点，向下的过程会被借过来）
            # print('before blance: ')
            # print_rbtree(node)
            node = self.rotateLeft(node)
            # print('after blance: ')
            # print_rbtree(node)

        # delmax 的平衡中 可能左右节点为红色的情况，左旋之后会产生连续两个红色子节点的情况
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        else:
            if self.isRed(node.left) and self.isRed(node.left.left):
                node = self.rotateRight(node)
            if self.isRed(node.left) and self.isRed(node.right):
                node = self.flipColor(node)
        return node

    def delMin(self):
        self.root = self._delMin(self.root)
        self.root.color = RBTreeNode.BLACK
        return self.root

    # 红黑树删除最小键
    def _delMin(self, node):
        # 最小节点是左子树的叶子节点，分两种情况考虑
        # 情况1：删除的是红色节点 - 直接删除，无需调整

        # 情况2：删除的是黑色节点 - 影响平衡，需调整
        # 情况2-1：兄弟节点是一个3-节点，可以借一个过来
        # 情况2-2：兄弟节点是一个2-节点，不能借。需向上递归进行调整
        #   具体方法为：节点删除后，父节点记作 double black保持平衡，结下来就是向上回溯然后消化掉double black的过程
        #             什么时候能消化，就是double black 的兄弟节点是一个3-节点，可以借一个过来，然后消化掉double black
        #             如果一直回溯到了根节点，就以根节点左旋，将拉下来的根节点置红，保持左右子树平衡

        # 上述常规思路是，先删除节点，然后在消化double black。
        # 也就是我没钱，但是我花了，一直奢着帐，然后一路向上找到能借我钱的人，我再把钱还了
        # 算法4 中提供了另外一种思路，就是我先把钱要过来，然后保证我有足够的钱花，最后我在把剩的钱，调整回去

        # 算法4 中提供的解决方案为在向下递归查找最小子节点的时候，始终保证当前节点不是一个2-节点。保证当前节点为一个3-节点或者一个临时的4-节点（算法4 定义的LLRB不允许4-节点）
        # 删除节点后向上调整临时的4-节点
        if node.left is None:
            return node.right

        # print("before move red left:")
        # print_rbtree(node)
        # 调整当前节点不为一个2-节点
        node = self._moveRedLeft(node)
        # print("after move red left:")
        # print_rbtree(node)

        node.left = self._delMin(node.left)

        # 递归向上的调整操作
        node.size = self.size(node.left) + self.size(node.right) + 1
        return self._blance(node)

    def delMax(self):
        self.root = self._delMax(self.root)
        self.root.color = RBTreeNode.BLACK
        return self.root

    # 红黑树删除最大键
    def _delMax(self, node):
        if node.right is None:
            return node.left

        print("before move right: ")
        print_rbtree(node)
        node = self._moveRedRight(node)
        print("after move right: ")
        print_rbtree(node)

        node.right = self._delMax(node.right)
        node.size = self.size(node.left) + self.size(node.right) + 1
        return self._blance(node)

    # 某个节点的后继节点
    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)
        self.root.color = RBTreeNode.BLACK
        return self.root

    # 红黑树删除指定节点
    def _delete(self, node, key):
        if node is None: 
            return None
        if key < node.key:
            node = self._moveRedLeft(node)
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node = self._moveRedRight(node)
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node = self._moveRedRight(node)
            # print_rbtree(self.root)
            successor = self._min(node.right)
            node.key, successor.key = successor.key, node.key
            node.val, successor.val = successor.val, node.val
            node.right = self._delMin(node.right)
        return self._blance(node)

    def log(self, msg=None):
        if msg:
            print(msg)
        print_rbtree(self.root)


# 操作部分
rbbst = RedBlackBst()

import random
# randlist = random.sample(range(10), 10)
randlist = [2, 5, 7, 3, 9, 4, 0, 1, 8, 6]
print("random list:", randlist)
for i in randlist:
    # print('put:', i, ":", i)
    rbbst.put(i, str(i))
    # print_rbtree(rbbst.root)

rbbst.log("init tree :")

while True:
    oper = input("operations: [delmin, delmax, del, put] ")
    if oper == 'delmin':
        rbbst.delMin()
    elif oper == 'delmax':
        rbbst.delMax()
    elif oper == 'del':
        key = input("delete (number):")
        rbbst.delete(int(key))
    elif oper == 'put':
        key = input("put (number):")
        rbbst.put(key, str(key))
    rbbst.log(oper)