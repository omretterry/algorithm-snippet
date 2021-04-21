class TreeNode():
    def __init__(self, key=None, val=None, size=1, left=None, right=None):
        self.key = key
        self.val = val
        self.size = size
        self.left = left
        self.right = right


# 红黑树节点
# 比普通的二叉树节点多了color属性，表示指向自身的链接的颜色
class RBTreeNode():
    RED = 'red'
    BLACK = 'black'
    
    def __init__(self, key=None, val=None, size=1, left=None, right=None, color=RBTreeNode.RED):
        self.key = key
        self.val = val
        self.size = size
        self.left = left
        self.right = right
        self.color = color
