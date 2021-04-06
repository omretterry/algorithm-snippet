# 二叉搜索树
# 实现简单，能够实现有序性的相关操作
# 可能退化成链表导致时间复杂度增加

import sys
sys.path.append('../../..')
from helper.TreeNode import TreeNode


class BST():
    def __init__(self):
        self.root = TreeNode()

