import math
class SegmentTree:
    def __init__(self, array, func, ide_ele):
        self.num = len(array)
        self.ide_ele = ide_ele
        self.segfunc = func
        self.tree = [self.ide_ele]*(self.num*2)
        for i in range(self.num):
            self.tree[self.num+i] = array[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[i*2], self.tree[i*2+1])
    
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k:
            k = k // 2
            self.tree[k] = self.segfunc(self.tree[k*2], self.tree[k*2+1])
    
    def query(self, l, r):
        l += self.num
        r += self.num
        res = self.ide_ele
        while l<=r:
            if l&1 == 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r&1 == 0:
                res = self.segfunc(res, self.tree[r])
                r -= 1
            l //=2
            r //=2
        return res

class BIT:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0]*(self.n+1)
        for i, num in enumerate(array):
            self.update(i+1, num)
    
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.tree[idx]
            idx -= idx&-idx
        return res_sum

    def update(self, idx, x):
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx&-idx
        return

def sum_(a, b):
    return a+b


if __name__ == '__main__':
    array = [0,1,2,3,4,5,6,7,8,9,10]
    st = SegmentTree(array, sum_, 0)
    # print('num of tree:', st.num)
    print('tree: ', st.tree)
    print('query(2, 5): ', st.query(2, 5))
    st.update(2, 5)
    # print('tree: ', st.tree)
    print('query(2, 5): ', st.query(2, 5))

    bit = BIT(array)
    # print('tree: ', bit.tree)
    print('query(2, 5): ', bit.query(5+1) - bit.query(1+1))