# 插入排序
# 插入排序所需的时间取决于输入中数组的初始顺序
# i 左边的元素都是排好序的，取l[i]，依次插入左边的有序数列中，
#   如果找到正确的位置，则直接返回
class Insertion():
    def __init__(self, l):
        self.l = l

    def sort(self):
        for i in range(1, len(self.l)):
            for j in range(i, 0, -1):
                if self.l[j] < self.l[j-1]:
                    self.l[j], self.l[j-1] = self.l[j-1], self.l[j]
                else:
                    break