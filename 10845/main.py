import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    mingling = sys.stdin.readline().split()
    if mingling[0] == 'push':
        queue.insert(0, mingling[1])
    elif mingling[0] == 'pop':
        if len(queue) == 0 : print("-1")
        else : 
            print(queue[-1])
            del queue[-1]
    elif mingling[0] == 'size':
        print(len(queue))
    elif mingling[0] == 'empty':
        if len(queue) == 0 : print("1")
        else : print("0")
    elif mingling[0] == 'front':
        if len(queue) == 0 : print("-1")
        else : print(queue[-1])
    elif mingling[0] == 'back':
        if len(queue) == 0 : print("-1")
        else : print(queue[0])
