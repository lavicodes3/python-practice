class Jar:
    def __init__(self,capacity=12):
        self.capacity=capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self,n):
        if self._size+n > self._capacity:
            raise ValueError
        self._size+=n

    def withdraw(self,n):
        if n > self._size:
            raise ValueError
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,n):
        if n < 0:
            raise ValueError
        self._capacity=n

    @property
    def size(self):
        return self._size


