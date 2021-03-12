# 自顶向下的归并算法

class Merge():
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

    def sort(self, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.sort(lo, mid)
        self.sort(mid + 1, hi)
        self.merge(lo,mid,hi)
        


l = [4, 5, 6, 1, 2, 3]
merge = Merge(l)
merge.sort(0 , len(l))
print(l)
