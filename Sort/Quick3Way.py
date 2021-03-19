# 3向切分快速排序
# 优化对于重复数字很多的数组，不必要的切分操作
import random


class Quick3Way:
    def __init__(self, l):
        self.l = l

    def sort(self):
        random.shuffle(self.l)
        self.quickSort(0, len(self.l) - 1)

    def quickSort(self, lo, hi):
        if lo >= hi:
            return
        lt, gt = lo, hi
        i = lt + 1
        t = self.l[lo]
        while i <= gt:
            if self.l[i] > t:
                self.l[i], self.l[gt] = self.l[gt], self.l[i]
                gt -= 1
            elif self.l[i] < t:
                self.l[i], self.l[lt] = self.l[lt], self.l[i]
                lt += 1
                i += 1
            else:
                i += 1
        # 相同元素的区间可以不用在进行切分
        self.quickSort(lo, lt - 1)
        self.quickSort(gt + 1, hi)


l = [3, 1, 2, 5, 6, 2, 2, 2, 7, 4, 9]
quick = Quick3Way(l)
quick.sort()
print(l)
