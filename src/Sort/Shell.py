# 希尔排序
# 基于插入排序，将数组分为h个组（递增序列）
# 先进行宏观上的排序，在对细节进行调整
# 利用的是插入排序对于相对有序队列的比较和交换次数相对较少的优势
# 目前的一个重要结论为 希尔排序的运行时间达不到平方级别

class Shell():
    def __init__(self, l):
        self.l = l

    def sort(self):
        h = 1
        while h < len(self.l) // 3:
            h = 3 * h + 1  # 递增序列为： 1，4，13，40...

        while h >= 1:
            for i in range(h, len(self.l)):
                for j in range(i, 0, -h):
                    if (self.l[j] < self.l[j-h]):
                        self.l[j], self.l[j-h] = self.l[j-h], self.l[j]
                    else:
                      break
            h = h // 3

l = [12,13,15,14,2,3,1,5,7,6,9,10,22,11,8]
shell = Shell(l)
shell.sort()
print(l)
