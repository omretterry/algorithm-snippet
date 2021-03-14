# 快速排序
# 选中一个区分点，大的放在右边，小的放在左边；
# 对左右部分做相同操作
# 时间复杂度： O(nlogn) 最坏可能会达到 O(n^2)（做随机规避）
# 比归并使用更少的空间，不稳定排序
# 一般认为在数组结构下，快排比归并移动更少的数组元素，所以快排的时间优于归并
import random


class Quick:
    def __init__(self, l):
        self.l = l

    def partition(self,lo,hi):
        target = self.l[lo]
        for i in range(lo, hi + 1):

    def sort(self):
        random.shuffle(self.l)
        self.sort(self, lo, hi)

    def sort(self, lo, hi):
        if lo > hi:
            return
        p = self.partition(lo ,hi )
        self.sort(lo, p)
        self.sort(p+1, hi)


l = [3, 1, 2]
quick = Quick(l)
quick.sort()
print(l)
