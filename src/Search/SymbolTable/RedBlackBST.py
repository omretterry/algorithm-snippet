# 红黑树
# 优点：最优的查找插入效率
# 链接需要额外的空间（同BST）
# 首先需要理解2-3树的节点拓展策略

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from helper.TreeNode import RBTreeNode


class RedBlackBst():
    def __init__(self):
        pass

    # 指向当前节点的链接是否为红链接
    def isRed(node):
      return node.color is RBTreeNode.RED

    

    def put(key, value):
