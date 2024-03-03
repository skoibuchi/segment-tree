import math
class SegmentTree:
    def __init__(self, array, func, ide_ele):
        n = len(array)
        self.num = 2**(n-1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = func
        self.tree = [self.ide_ele]*(self.num*2)
        for i in range(n):
            self.tree[self.num-1+i] = array[i]
        for i in range(self.num-2, -1, -1):
            self.tree[i] = self.segfunc(self.tree[i*2+1], self.tree[i*2+2])
    
    def update(self, k, x):
        k += self.num-1
        self.tree[k] = x
        while k:
            k = (k-1)//2
            self.tree[k] = self.segfunc(self.tree[k*2+1], self.tree[k*2+2])
    
    def query(self, l, r):
        l += self.num-1
        r += self.num-1
        ret = self.ide_ele
        while l<r:
            if l&1==0:
                ret = self.segfunc(ret, self.tree[l])
            if r&1==0:
                ret = self.segfunc(ret, self.tree[r-1])
                r -= 1
            l //=2
            r //=2
        return ret

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
    # print('tree: ', st.tree)
    print('query(1,4): ', st.query(1, 4))
    st.update(2, 3)
    # print('tree: ', st.tree)
    print('query(1,4): ', st.query(1, 4))

    bit = BIT(array)
    # print('tree: ', bit.tree)
    print('query(1,4): ', bit.query(4) - bit.query(0))