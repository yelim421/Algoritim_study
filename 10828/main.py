import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    mingling = sys.stdin.readline().split()
    if mingling[0] == 'push':
        stack.append(mingling[1])
    elif mingling[0] == 'pop':
        if len(stack) == 0 : print("-1")
        else : 
            print(stack[-1])
            stack.remove(stack[-1])
    elif mingling[0] == 'size':
        print(len(stack))
    elif mingling[0] == 'empty':
        if len(stack) == 0 : print("1")
        else : print("0")
    elif mingling[0] == 'top':
        if len(stack) == 0 : print("-1")
        else : print(stack[-1])