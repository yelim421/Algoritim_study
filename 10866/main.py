import sys
N = int(sys.stdin.readline())
deque = []
for i in range(N):
    mingling = sys.stdin.readline().split()
    if mingling[0] == 'push_front':
        deque.insert(0, mingling[1])
    if mingling[0] == 'push_back':
        deque.append(mingling[1])
    elif mingling[0] == 'pop_back':
        if len(deque) == 0 : print("-1")
        else : 
            print(deque[-1])
            del deque[-1]
    elif mingling[0] == 'pop_front':
        if len(deque) == 0 : print("-1")
        else : 
            print(deque[0])
            del deque[0]
    elif mingling[0] == 'size':
        print(len(deque))
    elif mingling[0] == 'empty':
        if len(deque) == 0 : print("1")
        else : print("0")
    elif mingling[0] == 'front':
        if len(deque) == 0 : print("-1")
        else : print(deque[0])
    elif mingling[0] == 'back':
        if len(deque) == 0 : print("-1")
        else : print(deque[-1])
