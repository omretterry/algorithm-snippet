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

    # 对向双指正写法
    def partition(self, lo, hi):
        i, j = lo + 1, hi
        t = self.l[lo]
        while i <= j:
            while self.l[i] < t and i < hi:
                i += 1
            while self.l[j] >= t and j > lo:
                j -= 1
            if i >= j:
                break
            self.l[i], self.l[j] = self.l[j], self.l[i]
        self.l[j], self.l[lo] = self.l[lo], self.l[j]
        return j

    def sort(self):
        # 避免最坏时间复杂度情况
        random.shuffle(self.l)
        self.quickSort(0, len(self.l) - 1)

    def quickSort(self, lo, hi):
        if lo >= hi:
            return
        p = self.partition(lo, hi)
        self.quickSort(lo, p-1)
        self.quickSort(p+1, hi)


# l = [3, 1, 2, 5, 6, 7, 4, 9]
l = [3, 2]
quick = Quick(l)
quick.sort()
print(l)
