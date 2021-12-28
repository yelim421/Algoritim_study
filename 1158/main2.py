from collections import deque
N ,K = map(int,input().split()) 

queue = deque()
res = []
for i in range(N):
    queue.append(i+1)

for _ in range(N):
    for j in range(K-1):
        queue.append(queue.popleft())

    res.append(queue.popleft())
    
print("<", end="")
print(", ".join(str(i) for i in res), end="")
print(">")