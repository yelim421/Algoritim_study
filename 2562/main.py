n = [0 for i in range(9)]
for i in range(9):
    n[i] = int(input())

print(max(n))
print(n.index(max(n))+1)