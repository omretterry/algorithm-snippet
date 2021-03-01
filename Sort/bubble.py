# 冒泡排序
# 相邻之间的元素两两比较，并把小的元素放到左边

class Bubble():
    def __init__(self, l):
        self.l = l

    def sort(self):
        # i 表示左边界，左边界依此右移
        for i in range(len(self.l)):
            for j in range(len(self.l) - 1, i, -1):
                if self.l[j] < self.l[j-1]:
                    self.l[j], self.l[j-1] = self.l[j-1], self.l[j]

l = [3, 2, 1, 4]
b = Bubble(l)
b.sort()
print(l)
