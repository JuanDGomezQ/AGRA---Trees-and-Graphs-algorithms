class SegmentTree(list):

    def __init__(self, arr):

        n = len(arr); N = 1; k = 0
        while N < n: N *= 2; k += 1
        st = [self.const()]*(2 * N - 1)
        st[N - 1:] = arr
        self[:] = st
        self.__create(0)
        self.__n = n
        self.__N = N
        self.__k = k

    def const(self): return float('inf')
    def parent(self, pos): return (pos - 1) >> 1
    def left(self, pos): return (pos << 1) + 1
    def right(self, pos): return (pos + 1) << 1
    def f(self, a, b): return min(a ,b)
    def len__(self): return self.__n
    def pop__(self):

        x = self[2**self.__k] - 1 + i
        self.update(self.__n - 1, self.const())
        self.n -= 1
        return x

    def __append__(self, x):
        if self.__n == self.N:
            A = [self[i] for i in range(2**(self.__k) - 1, 2**(self.__k) - 1 + self.__n)]
            A.append(x)
            self[:] = SegmentTree(A)
        else:
            self.update(self.__n, x)
            self.__n += 1


    def __create(self, i):

        ans = self.const()
        if (i < len(self)):
            ans = self[i] = self.f(self.f(self.__create(self.left(i)), self.__create(self.right(i))), self[i])
        return ans

    def update(self, i, x):
        
        pos = 2**(self.__k) - 1 + i
        self[pos] = x
        self.__update(self.parent(pos))

    def __update(self, i):
        if i >= 0:
            self[i] = self.f(self[self.left(i)], self[self.right(i)])
            if i != 0:
                self.__update(self.parent(i))

    def get(self, i, j):
        return self.__get(i, j, 0, self.__n, 0)

    def __get(self, i, j, low, high, pos):
        ans = self.const()
        if pos < len(self):
            if i == low and j == high: ans = self[pos]
            else:
                mid = (low + high) >> 1
                if i >= mid: ans = self.__get(i, j, mid, high, self.right(pos))
                elif j <= mid: ans = self.__get(i, j, low, mid, self.left(pos))
                else: ans = min(self.__get(i, mid, low, mid, self.left(pos)), self.__get(mid, j, mid, high, self.right(pos)))

        return ans