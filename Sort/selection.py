# 选择排序
# 遍历数组找出最小的元素放在列表头
# 时间复杂度 O(n^2)
# 特点： 1. 运行时间和输入的内容无关，比如随机大小的一组数，和一组相同的数，花的时间是相同的
#       2. 数据的移动次数是最少的， 移动次数为N
class Selection():
    def __init__(self, l):
        self.l = l

    def sort(self):
        for i in range(len(self.l)):
            m = i
            for j in range(i, len(self.l)):
                if self.l[j] < self.l[m]:
                    m = j
            self.l[i], self.l[m] = self.l[m], self.l[i]
