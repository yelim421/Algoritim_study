import math 
import time 


class Empty(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 5000

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def _resize(self, n):
        old = self._data
        self._data = [None] * n
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

N ,K = map(int,input().split()) 

start = time.time() 
math.factorial(100000) 

queue = ArrayQueue()
res = []
for i in range(N):
    queue.enqueue(i+1)

while not queue.is_empty():
    for i in range(K-1):
        queue.enqueue(queue.dequeue())

    res.append(queue.dequeue())
    
print("<", end="")
print(", ".join(str(i) for i in res), end="")
print(">")


end = time.time() 
print(f"{end - start:.5f} sec")