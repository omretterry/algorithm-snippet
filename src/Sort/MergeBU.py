# 自底向上的归并排序

class MergeBU():
    def __init__(self, l):
        self.l = l

    # 合并两个数组，满足：当两个数组都是有序的，那么合并的总数组有序
    def merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        t = self.l[::]
        for k in range(lo, hi + 1):
            if j > hi:
                self.l[k] = t[i]
                i += 1
            elif i > mid:
                self.l[k] = t[j]
                j += 1
            elif t[i] < t[j]:
                self.l[k] = t[i]
                i += 1
            else:
                self.l[k] = t[j]
                j += 1

    def sort(self):
        i = 1
        while i < len(self.l) + 1:
            for j in range(0, len(self.l)):
                self.merge(j, j + i - 1, min(len(self.l)-1, 2*i + j))
            i += i


l = [3, 1, 2, 6, 8, 5, 7, 9]
merge = MergeBU(l)
merge.sort()
print(l)
