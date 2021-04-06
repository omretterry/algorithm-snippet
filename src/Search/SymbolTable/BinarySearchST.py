# 基于数组的有序符号表
# 优先：最优的查找效率和空间需求，可进行有序性操作
# 缺点：插入操作很慢
class BinarySearchST():
    def __init__(self):
        self.keys = []
        self.vals = []

    def get(self, key):
        if len(self.keys) <= 0:
            return None
        i = self.rank(key)
        if i < len(self.keys) and self.keys[i] == key:
            return self.vals[i]
        return None

    # 返回小于这个key的个数
    def rank(self, key):
        lo, hi = 0, len(self.keys) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.keys[mid] > key:
                hi = mid - 1
            elif self.keys[mid] < key:
                lo = mid + 1
            else:
                return mid
        return lo

    def put(self, key, val):
        i = self.rank(key)
        if i < len(self.keys) and self.keys[i] == key:
            self.vals[i] = val
            return
        self.keys.insert(i, key)
        self.vals.insert(i, val)


# test
t = "searchexample"
st = BinarySearchST()
for i in range(len(t)):
    st.put(t[i], i)

for k in t:
    print(st.get(k))
